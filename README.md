# Readability Calculator

A Flesch-Kincaid Grade Level calculator for markdown documents. Analyzes text readability and identifies complex sentences.

## Features

- **Claude skill integration** - Analyze readability directly through Claude CLI with AI-powered suggestions
- **User-friendly GUI** with file selector and visual results (perfect for non-technical users)
- Calculates Flesch-Kincaid Grade Level for markdown documents
- Converts markdown to plain text (removes code blocks, links, images)
- Identifies sentences with grade level above 12
- Color-coded scores (green/orange/red) for easy interpretation
- Handles contractions, hyphenated words, and abbreviations
- Multiple encoding support (UTF-8, Latin-1, CP1252)
- Command-line interface available for automation

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### GUI Interface

Launch the graphical interface with a file selector and visual results display:

```bash
python3 launch_gui.py
```

Or double-click `launch_gui.py` in Finder (macOS) or File Explorer (Windows).

The GUI provides:
- **File selector button** - Browse and select markdown files
- **Visual score display** - Large, color-coded grade level (green/orange/red)
- **Grade interpretation** - Shows education level (elementary, high school, college, etc.)
- **Complex sentences list** - Scrollable list of sentences above grade 12

### Command Line Interface

For terminal users and automation:

```bash
python3 -m src.cli <markdown_file>
```

### Example

```bash
python3 -m src.cli document.md
```

### Output Format

The tool outputs:
1. Overall document grade level (numeric score)
2. List of complex sentences (grade level > 12), if any

Example output:
```
8.5

Complex sentences (grade level > 12):
- This is an extraordinarily complicated sentence with multisyllabic words.
- Another unnecessarily verbose sentence demonstrating excessive complexity.
```

### Claude Skill (AI-Powered Analysis)

For Claude CLI users, analyze readability with AI-powered suggestions:

```bash
# In Claude CLI, simply ask:
"Analyze the readability of document.md"
```

The Claude skill provides:
- Automated readability analysis
- AI-generated suggestions for simplifying complex sentences
- Specific rewrites in plain language
- Contextual recommendations based on your target audience
- Interactive revision workflow

**Example interaction:**
```
You: "Analyze test_complex.md and help me simplify it"

Claude:
  Analyzing test_complex.md...

  Grade Level: 24.4 (Graduate school level)

  Complex Sentences:
  1. "However, the aforementioned methodological paradigm necessitates..."
     → Suggested: "However, this approach requires collaboration between teams."

  2. "Furthermore, the implementation of sophisticated algorithmic..."
     → Suggested: "Additionally, these optimizations need powerful systems."

  Recommendations:
  - Target: 12.0 or below for general audiences
  - Simplify the 2 sentences above
  - Would you like me to rewrite the entire section?
```

**Setup**: The skill is located in `.claude/skills/readability/`. See `.claude/skills/readability/README.md` for details.

## Flesch-Kincaid Formula

The tool uses the Flesch-Kincaid Grade Level formula:

```
0.39 × (Total Words / Total Sentences) + 11.8 × (Total Syllables / Total Words) − 15.59
```

## Grade Level Interpretation

- 0-6: Elementary school level
- 7-8: Middle school level
- 9-12: High school level
- 13-16: College level
- 17+: Graduate school level

## Testing

Run the test suite:

```bash
python3 -m pytest tests/ -v
```

## Project Structure

```
readability-calculator/
├── launch_gui.py              # GUI launcher (double-click to run)
├── .claude/
│   └── skills/
│       └── readability/       # Claude skill for AI-powered analysis
│           ├── skill.yaml     # Skill configuration
│           ├── README.md      # Skill documentation
│           └── examples.md    # Usage examples
├── src/
│   ├── __init__.py
│   ├── gui.py                 # GUI interface with file selector
│   ├── syllable_counter.py    # Syllable counting algorithm
│   ├── text_analyzer.py       # Word and sentence counting
│   ├── markdown_parser.py     # Markdown to plain text conversion
│   ├── readability.py         # Flesch-Kincaid calculator
│   └── cli.py                 # Command-line interface
├── tests/
│   ├── test_syllable_counter.py
│   ├── test_text_analyzer.py
│   ├── test_markdown_parser.py
│   └── test_integration.py
├── requirements.txt
└── README.md
```

## Dependencies

- markdown >= 3.4.0
- beautifulsoup4 >= 4.12.0
- pytest >= 7.4.0 (for testing)
- tkinter (included with Python - used for GUI)

## Example Test Files

### Simple Document

```bash
python3 -m src.cli test_simple.md
# Output: 1.2
```

### Complex Document

```bash
python3 -m src.cli test_complex.md
# Output: 24.4
#
# Complex sentences (grade level > 12):
# - However, the aforementioned methodological paradigm necessitates...
# - Furthermore, the implementation of sophisticated algorithmic optimizations...
```

## How It Works

1. **Markdown Parsing**: Converts markdown to plain text, removing code blocks, links, and images
2. **Text Analysis**: Counts words and sentences, handling contractions and abbreviations
3. **Syllable Counting**: Counts syllables using vowel groups and handles silent 'e'
4. **Readability Calculation**: Applies Flesch-Kincaid formula to overall document
5. **Sentence Analysis**: Calculates readability for each sentence individually
6. **Output**: Displays overall score and highlights complex sentences (grade level > 12)

## Limitations

- Syllable counting is heuristic-based and may not be 100% accurate
- Abbreviation handling is limited to common titles (Dr., Mr., Mrs., etc.)
- Code blocks and technical content are removed from analysis
- Designed for English text only

## Error Handling

The tool handles:
- File not found errors
- Encoding issues (tries multiple encodings)
- Empty files (returns 0.0)
- Files with no readable text after markdown parsing (returns 0.0)

All errors are printed to stderr with exit code 1.
