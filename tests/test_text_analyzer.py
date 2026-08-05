"""Unit tests for text analyzer."""

import pytest
from src.text_analyzer import (
    count_words,
    count_sentences,
    split_into_sentences,
    extract_words
)


def test_count_words_basic():
    """Test basic word counting."""
    assert count_words("The cat sat on the mat.") == 6
    assert count_words("Hello world!") == 2
    assert count_words("One two three four five.") == 5


def test_count_words_contractions():
    """Test that contractions count as one word."""
    assert count_words("don't can't won't") == 3
    assert count_words("I'm going home.") == 3


def test_count_words_hyphenated():
    """Test that hyphenated words count as separate words."""
    assert count_words("state-of-the-art") == 4
    assert count_words("well-known") == 2


def test_count_words_filters_numbers():
    """Test that pure numbers are filtered out."""
    assert count_words("There are 123 apples.") == 3
    assert count_words("42 is the answer.") == 3


def test_count_words_empty():
    """Test empty text."""
    assert count_words("") == 0
    assert count_words("   ") == 0


def test_count_sentences_basic():
    """Test basic sentence counting."""
    assert count_sentences("This is a test.") == 1
    assert count_sentences("This is one. This is two.") == 2
    assert count_sentences("Question? Answer!") == 2


def test_count_sentences_abbreviations():
    """Test that abbreviations don't create false sentence breaks."""
    text = "Dr. Smith went to the store. He bought milk."
    assert count_sentences(text) == 2

    text = "Mr. Jones and Mrs. Smith met Prof. Brown."
    assert count_sentences(text) == 1


def test_count_sentences_multiple_punctuation():
    """Test multiple punctuation marks."""
    assert count_sentences("What?! No way!!") == 2


def test_count_sentences_empty():
    """Test empty text."""
    assert count_sentences("") == 0
    assert count_sentences("   ") == 0


def test_count_sentences_no_punctuation():
    """Test text without sentence-ending punctuation."""
    assert count_sentences("This is a test") == 1


def test_split_into_sentences():
    """Test sentence splitting."""
    text = "First sentence. Second sentence! Third sentence?"
    sentences = split_into_sentences(text)
    assert len(sentences) == 3
    assert sentences[0] == "First sentence"
    assert sentences[1] == "Second sentence"
    assert sentences[2] == "Third sentence"


def test_split_into_sentences_abbreviations():
    """Test sentence splitting with abbreviations."""
    text = "Dr. Smith is here. He is a doctor."
    sentences = split_into_sentences(text)
    assert len(sentences) == 2


def test_extract_words():
    """Test word extraction."""
    words = extract_words("The cat sat on the mat.")
    assert words == ["The", "cat", "sat", "on", "the", "mat"]


def test_extract_words_contractions():
    """Test word extraction with contractions."""
    words = extract_words("I don't think so.")
    assert "don't" in words


def test_extract_words_hyphenated():
    """Test word extraction with hyphenated words."""
    words = extract_words("state-of-the-art technology")
    assert "state" in words
    assert "of" in words
    assert "the" in words
    assert "art" in words
    assert "technology" in words


def test_extract_words_filters_numbers():
    """Test that pure numbers are filtered."""
    words = extract_words("There are 123 apples and 456 oranges.")
    assert "123" not in words
    assert "456" not in words
    assert "There" in words
    assert "are" in words
    assert "apples" in words
