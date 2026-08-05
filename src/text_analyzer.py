"""Text analysis functions for counting words and sentences."""

import re


def count_words(text: str) -> int:
    """
    Count words in text, filtering out numbers and non-alphabetic tokens.

    Contractions count as one word (don't, can't).
    Hyphenated words count as separate words.

    Args:
        text: The text to analyze

    Returns:
        Number of words
    """
    if not text:
        return 0

    # Split on whitespace
    tokens = text.split()

    word_count = 0
    for token in tokens:
        # Remove punctuation except apostrophes and hyphens
        cleaned = re.sub(r"[^\w'\-]", '', token)

        # Skip if empty after cleaning
        if not cleaned:
            continue

        # Skip if purely numeric
        if cleaned.replace('-', '').isdigit():
            continue

        # Handle hyphenated words - count as separate words
        if '-' in cleaned:
            parts = [p for p in cleaned.split('-') if p and not p.isdigit()]
            # Count parts that contain at least one letter
            for part in parts:
                if any(c.isalpha() for c in part):
                    word_count += 1
        else:
            # Count if contains at least one letter
            if any(c.isalpha() for c in cleaned):
                word_count += 1

    return word_count


def count_sentences(text: str) -> int:
    """
    Count sentences in text.

    Sentences end with '.', '!', or '?'
    Handles common abbreviations (Dr., Mr., Mrs., etc.)

    Args:
        text: The text to analyze

    Returns:
        Number of sentences (minimum 1 if text is non-empty)
    """
    if not text or not text.strip():
        return 0

    # Replace common abbreviations to avoid false sentence breaks
    text = re.sub(r'\bDr\.', 'Dr', text)
    text = re.sub(r'\bMr\.', 'Mr', text)
    text = re.sub(r'\bMrs\.', 'Mrs', text)
    text = re.sub(r'\bMs\.', 'Ms', text)
    text = re.sub(r'\bProf\.', 'Prof', text)
    text = re.sub(r'\bSr\.', 'Sr', text)
    text = re.sub(r'\bJr\.', 'Jr', text)

    # Split on sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)

    # Filter out empty sentences
    sentences = [s.strip() for s in sentences if s.strip()]

    # Return at least 1 if there's any text
    return max(1, len(sentences))


def split_into_sentences(text: str) -> list[str]:
    """
    Split text into individual sentences.

    Args:
        text: The text to split

    Returns:
        List of sentence strings
    """
    if not text or not text.strip():
        return []

    # Normalize whitespace: replace single newlines with spaces, keep paragraph breaks
    # This handles sentences that span multiple lines in markdown
    text = re.sub(r'\n\n+', '\n\n', text)  # Normalize multiple newlines to double newline
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)  # Single newlines become spaces

    # Replace common abbreviations to avoid false sentence breaks
    text = re.sub(r'\bDr\.', 'Dr', text)
    text = re.sub(r'\bMr\.', 'Mr', text)
    text = re.sub(r'\bMrs\.', 'Mrs', text)
    text = re.sub(r'\bMs\.', 'Ms', text)
    text = re.sub(r'\bProf\.', 'Prof', text)
    text = re.sub(r'\bSr\.', 'Sr', text)
    text = re.sub(r'\bJr\.', 'Jr', text)

    # Split on sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)

    # Filter out empty sentences and strip whitespace
    # Also filter out single-word items (likely headers or fragments)
    filtered_sentences = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        # Skip single-word items (headers/fragments)
        words = s.split()
        if len(words) < 2:
            continue
        filtered_sentences.append(s)

    return filtered_sentences


def extract_words(text: str) -> list[str]:
    """
    Extract individual words from text for syllable counting.

    Args:
        text: The text to extract words from

    Returns:
        List of word strings
    """
    if not text:
        return []

    # Split on whitespace
    tokens = text.split()

    words = []
    for token in tokens:
        # Remove punctuation except apostrophes and hyphens
        cleaned = re.sub(r"[^\w'\-]", '', token)

        if not cleaned:
            continue

        # Skip purely numeric tokens
        if cleaned.replace('-', '').isdigit():
            continue

        # Handle hyphenated words
        if '-' in cleaned:
            parts = [p for p in cleaned.split('-') if p and not p.isdigit()]
            for part in parts:
                if any(c.isalpha() for c in part):
                    words.append(part)
        else:
            if any(c.isalpha() for c in cleaned):
                words.append(cleaned)

    return words
