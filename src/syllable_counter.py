"""Syllable counting algorithm for readability analysis."""

import re


def count_syllables(word: str) -> int:
    """
    Count syllables in a word using vowel group method.

    Algorithm:
    - Count vowel groups (consecutive vowels = 1 syllable)
    - Subtract silent 'e' at word end (except for -le endings)
    - Minimum 1 syllable per word

    Args:
        word: The word to count syllables in

    Returns:
        Number of syllables (minimum 1)
    """
    if not word:
        return 0

    # Normalize: lowercase and remove non-alphabetic characters
    word = word.lower().strip()
    word = re.sub(r'[^a-z]', '', word)

    if not word:
        return 0

    # Count vowel groups
    vowel_groups = 0
    previous_was_vowel = False

    for char in word:
        is_vowel = char in 'aeiouy'
        if is_vowel and not previous_was_vowel:
            vowel_groups += 1
        previous_was_vowel = is_vowel

    # Handle silent 'e' at the end
    # Don't subtract for words ending in 'le' (like "table", "simple")
    if len(word) >= 2 and word.endswith('e') and not word.endswith('le'):
        # Check if the 'e' is silent (preceded by a consonant)
        if word[-2] not in 'aeiouy':
            vowel_groups -= 1

    # Ensure at least 1 syllable
    return max(1, vowel_groups)
