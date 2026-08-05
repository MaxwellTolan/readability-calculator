"""Unit tests for syllable counter."""

import pytest
from src.syllable_counter import count_syllables


def test_basic_words():
    """Test syllable counting for common words."""
    assert count_syllables("hello") == 2
    assert count_syllables("world") == 1
    assert count_syllables("beautiful") == 3
    assert count_syllables("cat") == 1
    assert count_syllables("dog") == 1


def test_silent_e():
    """Test silent 'e' handling."""
    assert count_syllables("make") == 1
    assert count_syllables("take") == 1
    assert count_syllables("home") == 1
    assert count_syllables("time") == 1


def test_le_ending():
    """Test words ending in 'le' (e is not silent)."""
    assert count_syllables("table") == 2
    assert count_syllables("simple") == 2
    assert count_syllables("people") == 2
    assert count_syllables("bottle") == 2


def test_vowel_groups():
    """Test consecutive vowels count as one syllable."""
    assert count_syllables("read") == 1
    assert count_syllables("team") == 1
    assert count_syllables("beat") == 1
    assert count_syllables("coin") == 1


def test_edge_cases():
    """Test edge cases."""
    assert count_syllables("") == 0
    assert count_syllables("a") == 1
    assert count_syllables("I") == 1
    assert count_syllables("the") == 1


def test_complex_words():
    """Test longer, more complex words."""
    assert count_syllables("development") == 4
    assert count_syllables("implementation") == 5
    assert count_syllables("understanding") == 4
    assert count_syllables("extraordinary") == 5


def test_normalization():
    """Test that words are normalized properly."""
    assert count_syllables("HELLO") == 2
    assert count_syllables("WoRlD") == 1
    assert count_syllables("test123") == 1
    assert count_syllables("test-word") == 2  # Hyphen removed, becomes 'testword'
