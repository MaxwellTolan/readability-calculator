"""Unit tests for markdown parser."""

import pytest
import tempfile
import os
from src.markdown_parser import load_markdown_file, markdown_to_plaintext


def test_markdown_to_plaintext_basic():
    """Test basic markdown to plaintext conversion."""
    markdown = "# Hello\n\nThis is a test."
    result = markdown_to_plaintext(markdown)
    assert "Hello" in result
    assert "This is a test." in result


def test_markdown_to_plaintext_headers():
    """Test that headers are converted to plain text."""
    markdown = "# Header 1\n## Header 2\n### Header 3"
    result = markdown_to_plaintext(markdown)
    assert "Header 1" in result
    assert "Header 2" in result
    assert "Header 3" in result
    assert "#" not in result


def test_markdown_to_plaintext_links():
    """Test that links are converted to just text."""
    markdown = "Check out [this link](https://example.com) for more."
    result = markdown_to_plaintext(markdown)
    assert "this link" in result
    assert "https://example.com" not in result
    assert "[" not in result
    assert "]" not in result


def test_markdown_to_plaintext_images():
    """Test that images are removed."""
    markdown = "Here is an image: ![alt text](image.png)"
    result = markdown_to_plaintext(markdown)
    assert "Here is an image:" in result
    assert "alt text" not in result
    assert "image.png" not in result


def test_markdown_to_plaintext_code_blocks():
    """Test that code blocks are removed."""
    markdown = """# Title

Some text.

```python
def hello():
    print("hello")
```

More text."""
    result = markdown_to_plaintext(markdown)
    assert "Title" in result
    assert "Some text." in result
    assert "More text." in result
    assert "def hello" not in result
    assert "print" not in result


def test_markdown_to_plaintext_inline_code():
    """Test that inline code is removed."""
    markdown = "Use the `print()` function to output text."
    result = markdown_to_plaintext(markdown)
    assert "Use the" in result
    assert "function to output text." in result
    assert "`" not in result


def test_markdown_to_plaintext_lists():
    """Test that lists are converted to plain text."""
    markdown = """- Item 1
- Item 2
- Item 3"""
    result = markdown_to_plaintext(markdown)
    assert "Item 1" in result
    assert "Item 2" in result
    assert "Item 3" in result


def test_markdown_to_plaintext_empty():
    """Test empty markdown."""
    assert markdown_to_plaintext("") == ""
    assert markdown_to_plaintext("   ") == ""


def test_load_markdown_file():
    """Test loading markdown file with UTF-8 encoding."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write("# Test\n\nThis is a test.")
        temp_path = f.name

    try:
        content = load_markdown_file(temp_path)
        assert "# Test" in content
        assert "This is a test." in content
    finally:
        os.unlink(temp_path)


def test_load_markdown_file_not_found():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        load_markdown_file("/path/that/does/not/exist.md")


def test_markdown_to_plaintext_complex():
    """Test complex markdown document."""
    markdown = """# Research Paper

## Introduction

This is the [introduction](https://example.com) with a link.

## Methods

We used the following approach:

```python
def analyze():
    return "data"
```

The `analyze()` function processes data.

## Results

- Finding 1
- Finding 2
- Finding 3

![Chart](chart.png)

## Conclusion

This concludes the paper.
"""
    result = markdown_to_plaintext(markdown)

    # Should include text
    assert "Research Paper" in result
    assert "Introduction" in result
    assert "introduction" in result
    assert "Methods" in result
    assert "Results" in result
    assert "Conclusion" in result

    # Should NOT include code, URLs, or markdown syntax
    assert "def analyze" not in result
    assert "https://example.com" not in result
    assert "chart.png" not in result
    assert "```" not in result
