"""Flesch-Kincaid Grade Level readability calculator."""

from .syllable_counter import count_syllables
from .text_analyzer import count_words, count_sentences, split_into_sentences, extract_words


def calculate_readability(text: str) -> float:
    """
    Calculate Flesch-Kincaid Grade Level for text.

    Formula: 0.39 × (Total Words / Total Sentences) + 11.8 × (Total Syllables / Total Words) − 15.59

    Args:
        text: Plain text to analyze

    Returns:
        Grade level score (rounded to 1 decimal place)
    """
    if not text or not text.strip():
        return 0.0

    words = count_words(text)
    sentences = count_sentences(text)

    if words == 0 or sentences == 0:
        return 0.0

    # Extract words and count syllables
    word_list = extract_words(text)
    syllables = sum(count_syllables(word) for word in word_list)

    # Calculate components
    avg_words_per_sentence = words / sentences
    avg_syllables_per_word = syllables / words if words > 0 else 0

    # Apply Flesch-Kincaid formula
    score = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59

    return round(score, 1)


def analyze_sentences(text: str) -> list[tuple[str, float]]:
    """
    Analyze each sentence and return grade level scores.

    Args:
        text: Plain text to analyze

    Returns:
        List of (sentence_text, grade_level) tuples
    """
    if not text or not text.strip():
        return []

    sentence_list = split_into_sentences(text)
    results = []

    for sentence in sentence_list:
        sentence = sentence.strip()
        if not sentence:
            continue

        score = calculate_readability(sentence)
        results.append((sentence, score))

    return results


def get_complex_sentences(text: str, threshold: float = 12.0) -> list[str]:
    """
    Return sentences with grade level above threshold.

    Args:
        text: Plain text to analyze
        threshold: Grade level threshold (default 12.0)

    Returns:
        List of complex sentence strings
    """
    all_sentences = analyze_sentences(text)
    return [sent for sent, score in all_sentences if score > threshold]
