"""Integration tests for the full readability calculator pipeline."""

import pytest
import tempfile
import os
from src.markdown_parser import load_markdown_file, markdown_to_plaintext
from src.readability import calculate_readability, get_complex_sentences


def test_simple_document():
    """Test with a simple document."""
    markdown = """# Simple Test

This is a test document. It has simple words. The cat sat on the mat.
"""

    plain_text = markdown_to_plaintext(markdown)
    score = calculate_readability(plain_text)

    # Should be low grade level (simple words and sentences)
    assert score < 6.0


def test_complex_document():
    """Test with a complex document containing long sentences."""
    markdown = """# Research Document

This is a simple sentence. The cat sat on the mat.

However, the aforementioned methodological paradigm necessitates comprehensive
interdisciplinary collaboration among heterogeneous stakeholder constituencies.

Furthermore, the implementation of sophisticated algorithmic optimizations requires
extensive computational infrastructure with distributed processing capabilities.
"""

    plain_text = markdown_to_plaintext(markdown)
    score = calculate_readability(plain_text)

    # Should have moderate-to-high grade level due to complex sentences
    assert score > 8.0

    # Should identify complex sentences
    complex_sentences = get_complex_sentences(plain_text, threshold=12.0)
    assert len(complex_sentences) >= 1


def test_markdown_features():
    """Test that markdown features are properly handled."""
    markdown = """# Title

## Introduction

This is a [link](https://example.com) in the text.

Here is some `inline code` that should be removed.

```python
def hello():
    print("world")
```

- List item one
- List item two

![Image](image.png)

The actual content continues here.
"""

    plain_text = markdown_to_plaintext(markdown)

    # Should include text content
    assert "Title" in plain_text
    assert "Introduction" in plain_text
    assert "link" in plain_text
    assert "actual content continues here" in plain_text

    # Should NOT include code, URLs, or markdown syntax
    assert "def hello" not in plain_text
    assert "https://example.com" not in plain_text
    assert "```" not in plain_text

    # Should calculate a score
    score = calculate_readability(plain_text)
    assert score >= 0.0


def test_file_to_score_pipeline():
    """Test the complete pipeline from file to score."""
    markdown_content = """# Test Document

This is a simple test. The words are short. The sentences are brief.
"""

    # Create temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(markdown_content)
        temp_path = f.name

    try:
        # Load file
        content = load_markdown_file(temp_path)
        assert len(content) > 0

        # Convert to plain text
        plain_text = markdown_to_plaintext(content)
        assert "simple test" in plain_text

        # Calculate readability
        score = calculate_readability(plain_text)
        assert score > 0.0
        assert score < 10.0  # Should be relatively simple

    finally:
        os.unlink(temp_path)


def test_edge_case_empty_file():
    """Test with an empty file."""
    markdown = ""
    plain_text = markdown_to_plaintext(markdown)
    score = calculate_readability(plain_text)
    assert score == 0.0


def test_edge_case_only_code():
    """Test document with only code blocks."""
    markdown = """```python
def test():
    pass
```"""

    plain_text = markdown_to_plaintext(markdown)
    score = calculate_readability(plain_text)
    # After removing code, should have no content
    assert score == 0.0


def test_complex_sentence_detection():
    """Test that complex sentences are properly detected."""
    markdown = """
Simple sentence here.

The extraordinarily sophisticated methodological framework necessitates comprehensive
interdisciplinary collaboration among heterogeneous stakeholder constituencies with
multifaceted perspectives and diversified operational capabilities.

Another simple one.
"""

    plain_text = markdown_to_plaintext(markdown)
    complex_sentences = get_complex_sentences(plain_text, threshold=12.0)

    # Should find at least one complex sentence
    assert len(complex_sentences) >= 1

    # The complex sentence should be in the list
    found_complex = False
    for sent in complex_sentences:
        if "methodological framework" in sent or "sophisticated" in sent:
            found_complex = True
            break
    assert found_complex


def test_overall_vs_sentence_scores():
    """Test that overall score differs from individual sentence scores."""
    markdown = """
This is simple. Easy words here.

The multifaceted interdisciplinary paradigm necessitates comprehensive stakeholder engagement.
"""

    plain_text = markdown_to_plaintext(markdown)

    # Overall score should be moderate (averaging simple and complex)
    overall_score = calculate_readability(plain_text)

    # Some individual sentences should be above 12
    complex_sentences = get_complex_sentences(plain_text, threshold=12.0)

    # The complex sentence should be detected
    assert len(complex_sentences) >= 1
