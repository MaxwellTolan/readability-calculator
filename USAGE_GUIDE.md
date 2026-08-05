# Quick Start Guide for Non-Technical Users

## What is this tool?

This tool analyzes markdown documents and tells you how difficult they are to read. It gives you a grade level score (like "8th grade" or "college level") and highlights any sentences that are too complex.

## How to Use (3 Easy Steps)

### Step 1: Install Python Requirements

Open Terminal (macOS) or Command Prompt (Windows) and navigate to the readability-calculator folder, then run:

```bash
pip install -r requirements.txt
```

You only need to do this once.

### Step 2: Launch the Application

**Option A: Double-click method**
- Find the file named `launch_gui.py`
- Double-click it to open the application

**Option B: Terminal method**
```bash
python3 launch_gui.py
```

### Step 3: Analyze Your Document

1. Click the **"Select Markdown File"** button
2. Browse to your markdown file (.md file)
3. Click **"Analyze"**
4. View your results!

## Understanding Your Results

### Grade Level Score

The big number at the top is your document's grade level:

- **0-6**: Elementary school level (very easy to read)
- **7-8**: Middle school level (easy to read)
- **9-12**: High school level (moderate difficulty)
- **13-16**: College level (challenging)
- **17+**: Graduate school level (very challenging)

The color helps too:
- **Green** = Easy to read
- **Orange** = Moderately difficult
- **Red** = Challenging

### Complex Sentences

Below the score, you'll see a list of sentences that are above 12th grade level. These are sentences you might want to simplify if you want your document to be more accessible.

If you see "No complex sentences found" - great! Your document is written at or below 12th grade level throughout.

## Tips for Better Readability

If your score is higher than you want:

1. **Break up long sentences** - Look at the complex sentences listed and split them into shorter ones
2. **Use simpler words** - Replace big words with shorter alternatives where possible
3. **Avoid jargon** - Use plain language instead of technical terms when possible
4. **Check again** - Re-analyze your document after making changes to see if the score improved

## Troubleshooting

**"No file selected" error**
- Make sure you clicked "Select Markdown File" and chose a .md file

**"File contains no readable text" error**
- Your file might be mostly code blocks
- The tool removes code when analyzing, so documents with only code won't work

**Application won't start**
- Make sure you installed the requirements (Step 1 above)
- Make sure you have Python 3 installed on your computer

## Need Help?

If you encounter issues, check that:
1. Python 3 is installed on your computer
2. You ran `pip install -r requirements.txt`
3. Your file is a markdown (.md) file
4. Your file contains actual text content (not just code blocks)
