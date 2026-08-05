# Readability Analysis Skill

A Claude skill for analyzing markdown documents using the Flesch-Kincaid readability calculator.

## Installation

This skill is located in the readability-calculator project directory. To use it:

1. Ensure you're in the `/Users/maxwelltolan/readability-calculator/` directory
2. Make sure dependencies are installed: `pip install -r requirements.txt`

## Usage

Invoke the skill by asking Claude to analyze readability:

```
Analyze the readability of document.md
```

```
Check the reading level of my blog post
```

```
What's the Flesch-Kincaid score for article.md?
```

```
Help me simplify the complex sentences in report.md
```

## What It Does

The skill will:

1. **Run analysis** - Calculate the Flesch-Kincaid Grade Level for your markdown document
2. **Show the score** - Display the overall grade level (0-20+)
3. **List complex sentences** - Identify sentences above grade 12
4. **Provide recommendations** - Suggest specific rewrites and improvements
5. **Explain the results** - Interpret what the score means for your audience

## Example Session

**User**: "Analyze the readability of test_complex.md"

**Claude**:
```
Running readability analysis...

Grade Level: 24.4 (Graduate school level)

Complex Sentences Found:

1. "However, the aforementioned methodological paradigm necessitates comprehensive
   interdisciplinary collaboration among heterogeneous stakeholder constituencies."

   Suggested rewrite: "However, this approach requires collaboration between
   different teams and stakeholders."

2. "Furthermore, the implementation of sophisticated algorithmic optimizations
   requires extensive computational infrastructure with distributed processing
   capabilities."

   Suggested rewrite: "Additionally, implementing these optimizations requires
   powerful computing systems with distributed processing."

Recommendations:
- Your document is at graduate school level (24.4)
- Simplify the 2 complex sentences above to reach high school level
- Target score: 12.0 or below for general audiences
```

## Features

- Automatically navigates to project directory
- Runs Python CLI tool
- Interprets results in user-friendly language
- Provides actionable suggestions
- Offers to rewrite complex sentences

## Grade Level Reference

- **0-6**: Elementary school (very accessible)
- **7-8**: Middle school (easy to read)
- **9-12**: High school (moderate difficulty)
- **13-16**: College (challenging)
- **17+**: Graduate school (very challenging)

## Tips for Best Results

1. **Specify the file path** - Provide the full path or filename
2. **Ask for help** - Request suggestions for specific sentences
3. **Iterate** - Analyze, revise, and re-analyze until you reach your target score

## Technical Details

- **Tool**: Flesch-Kincaid Grade Level calculator
- **Formula**: `0.39 × (Words/Sentences) + 11.8 × (Syllables/Words) - 15.59`
- **Input**: Markdown files (.md)
- **Output**: Grade level + complex sentences list
