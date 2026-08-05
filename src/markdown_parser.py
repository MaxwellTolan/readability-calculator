"""Markdown parsing functions to convert markdown to plain text."""

import re
import markdown
from bs4 import BeautifulSoup


def load_markdown_file(file_path: str) -> str:
    """
    Load markdown file with encoding fallback.

    Tries utf-8, then latin-1, then cp1252.

    Args:
        file_path: Path to markdown file

    Returns:
        File contents as string

    Raises:
        FileNotFoundError: If file doesn't exist
        Exception: If file cannot be read with any encoding
    """
    encodings = ['utf-8', 'latin-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            raise

    raise Exception(f"Could not read file {file_path} with any supported encoding")


def markdown_to_plaintext(markdown_text: str) -> str:
    """
    Convert markdown text to plain text for analysis.

    - Removes code blocks (fenced and indented)
    - Strips markdown link syntax [text](url) -> text
    - Removes images ![alt](url)
    - Converts headers to plain text
    - Extracts text from HTML conversion

    Args:
        markdown_text: Markdown-formatted text

    Returns:
        Plain text suitable for readability analysis
    """
    if not markdown_text:
        return ""

    # Remove fenced code blocks (```...```)
    markdown_text = re.sub(r'```[\s\S]*?```', '', markdown_text)

    # Remove inline code (`...`)
    markdown_text = re.sub(r'`[^`]+`', '', markdown_text)

    # Remove images ![alt](url)
    markdown_text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', markdown_text)

    # Convert links [text](url) to just text
    markdown_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', markdown_text)

    # Remove HTML comments
    markdown_text = re.sub(r'<!--[\s\S]*?-->', '', markdown_text)

    # Convert markdown to HTML
    html = markdown.markdown(markdown_text)

    # Use BeautifulSoup to extract plain text
    soup = BeautifulSoup(html, 'html.parser')
    plain_text = soup.get_text()

    # Clean up extra whitespace
    plain_text = re.sub(r'\n\s*\n', '\n\n', plain_text)  # Multiple newlines to double newline
    plain_text = plain_text.strip()

    return plain_text
