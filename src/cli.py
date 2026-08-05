"""Command-line interface for readability calculator."""

import sys
import argparse
from .markdown_parser import load_markdown_file, markdown_to_plaintext
from .readability import calculate_readability, get_complex_sentences


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Calculate Flesch-Kincaid readability score for markdown files'
    )
    parser.add_argument('file', help='Path to markdown file')
    args = parser.parse_args()

    try:
        # Load and parse markdown file
        markdown_content = load_markdown_file(args.file)
        plain_text = markdown_to_plaintext(markdown_content)

        if not plain_text or not plain_text.strip():
            print("0.0", file=sys.stderr)
            sys.exit(1)

        # Calculate overall readability score
        score = calculate_readability(plain_text)
        print(score)

        # Find and display complex sentences
        complex_sentences = get_complex_sentences(plain_text, threshold=12.0)
        if complex_sentences:
            print("\nComplex sentences (grade level > 12):")
            for sentence in complex_sentences:
                print(f"- {sentence}")

        sys.exit(0)

    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
