# Readability Skill Examples

## Basic Usage

### Example 1: Simple Analysis Request

**User**: "Analyze the readability of test_simple.md"

**Expected Response**:
- Run `python3 -m src.cli test_simple.md`
- Report grade level (should be ~1.2)
- Explain that it's very accessible (elementary level)
- Note that no complex sentences were found

### Example 2: Complex Document Analysis

**User**: "Check the reading level of test_complex.md"

**Expected Response**:
- Run `python3 -m src.cli test_complex.md`
- Report grade level (should be ~24.4)
- List 2 complex sentences
- Provide specific suggestions for simplification
- Offer to rewrite the complex sentences

### Example 3: Requesting Simplification

**User**: "Analyze my_document.md and help me simplify complex sentences"

**Expected Response**:
- Run analysis
- Show grade level and complex sentences
- Provide rewritten versions of each complex sentence
- Explain the changes made (shorter words, split sentences, etc.)
- Offer to analyze again after user makes edits

## Advanced Usage

### Example 4: Target Audience

**User**: "I need this document at high school reading level. Analyze blog_post.md"

**Expected Response**:
- Run analysis
- Compare current score to target (12.0 for high school)
- Prioritize sentences that need simplification
- Calculate how much the score needs to drop
- Provide strategic recommendations

### Example 5: Before/After Comparison

**User**: "I revised the document. Can you check if the readability improved?"

**Expected Response**:
- Run analysis on revised version
- Compare to previous score (if available)
- Celebrate improvements
- Identify remaining issues if score still above target

## Command Variations

Users might ask in various ways:

- "What's the Flesch-Kincaid score for X?"
- "Is this document easy to read?"
- "Check reading level"
- "Analyze readability"
- "Help me simplify this"
- "What grade level is this?"
- "Find complex sentences in X"

All should trigger the readability skill.

## Integration with Writing Workflow

### Workflow Example

1. **Draft**: User writes initial content
2. **Analyze**: "Analyze draft.md"
3. **Review**: Claude shows score and complex sentences
4. **Revise**: User simplifies based on suggestions
5. **Re-analyze**: "Check draft.md again"
6. **Iterate**: Repeat until target score reached

## Expected Output Format

```
Analyzing: [filename]

Grade Level: [X.X] ([interpretation])

[If score > 12]
Complex Sentences (Grade Level > 12):

1. "[sentence text]"
   → Suggested: "[simplified version]"

2. "[sentence text]"
   → Suggested: "[simplified version]"

Recommendations:
- [Specific actionable advice]
- [Target score guidance]
- [Offer to help with revisions]

[If score ≤ 12]
Great! No complex sentences found. Your document is accessible at
[grade level] or below.
```

## Error Handling

### File Not Found

**User**: "Analyze nonexistent.md"

**Expected Response**:
- Attempt to run analysis
- Report file not found error
- Ask user to provide correct path
- Optionally list available .md files in directory

### Empty or Code-Only File

**User**: "Analyze code_file.md"

**Expected Response**:
- Run analysis
- Report that file contains no readable text
- Explain that code blocks are removed before analysis
- Suggest adding prose content
