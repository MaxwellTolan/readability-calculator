"""GUI interface for readability calculator."""

import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from tkinter import ttk
import os
from .markdown_parser import load_markdown_file, markdown_to_plaintext
from .readability import calculate_readability, get_complex_sentences


class ReadabilityCalculatorGUI:
    """GUI application for readability calculator."""

    def __init__(self, root):
        """Initialize the GUI."""
        self.root = root
        self.root.title("Readability Calculator")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Configure grid weights for responsive layout
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.selected_file = None
        self.create_widgets()

    def create_widgets(self):
        """Create all GUI widgets."""
        # Top frame for file selection
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.grid(row=0, column=0, sticky="ew")
        top_frame.grid_columnconfigure(1, weight=1)

        # File selection button
        select_btn = ttk.Button(
            top_frame,
            text="Select Markdown File",
            command=self.select_file,
            width=20
        )
        select_btn.grid(row=0, column=0, padx=5, pady=5)

        # Selected file label
        self.file_label = ttk.Label(
            top_frame,
            text="No file selected",
            foreground="gray"
        )
        self.file_label.grid(row=0, column=1, sticky="w", padx=5)

        # Analyze button
        self.analyze_btn = ttk.Button(
            top_frame,
            text="Analyze",
            command=self.analyze_file,
            state="disabled",
            width=15
        )
        self.analyze_btn.grid(row=0, column=2, padx=5, pady=5)

        # Separator
        separator = ttk.Separator(self.root, orient="horizontal")
        separator.grid(row=1, column=0, sticky="ew", pady=5)

        # Results frame
        results_frame = ttk.Frame(self.root, padding="10")
        results_frame.grid(row=2, column=0, sticky="nsew")
        results_frame.grid_rowconfigure(1, weight=1)
        results_frame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        # Score display
        score_frame = ttk.Frame(results_frame)
        score_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        ttk.Label(
            score_frame,
            text="Grade Level:",
            font=("TkDefaultFont", 11, "bold")
        ).grid(row=0, column=0, sticky="w")

        self.score_label = ttk.Label(
            score_frame,
            text="--",
            font=("TkDefaultFont", 24, "bold"),
            foreground="#2e7d32"
        )
        self.score_label.grid(row=0, column=1, padx=10)

        self.interpretation_label = ttk.Label(
            score_frame,
            text="",
            font=("TkDefaultFont", 10),
            foreground="gray"
        )
        self.interpretation_label.grid(row=0, column=2, sticky="w")

        # Complex sentences display
        ttk.Label(
            results_frame,
            text="Complex Sentences (Grade Level > 12):",
            font=("TkDefaultFont", 11, "bold")
        ).grid(row=1, column=0, sticky="w", pady=(0, 5))

        # Scrolled text for complex sentences
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=("TkDefaultFont", 10),
            state="disabled"
        )
        self.results_text.grid(row=2, column=0, sticky="nsew")

        # Configure text tags for formatting
        self.results_text.tag_config("bullet", lmargin1=20, lmargin2=40)
        self.results_text.tag_config("none", foreground="gray", font=("TkDefaultFont", 10, "italic"))

    def select_file(self):
        """Open file dialog to select markdown file."""
        filename = filedialog.askopenfilename(
            title="Select Markdown File",
            filetypes=[
                ("Markdown files", "*.md"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )

        if filename:
            self.selected_file = filename
            # Display just the filename, not full path
            display_name = os.path.basename(filename)
            self.file_label.config(text=display_name, foreground="black")
            self.analyze_btn.config(state="normal")

    def analyze_file(self):
        """Analyze the selected file and display results."""
        if not self.selected_file:
            messagebox.showerror("Error", "Please select a file first.")
            return

        try:
            # Load and parse markdown
            markdown_content = load_markdown_file(self.selected_file)
            plain_text = markdown_to_plaintext(markdown_content)

            if not plain_text or not plain_text.strip():
                messagebox.showerror(
                    "Error",
                    "The file contains no readable text after removing code blocks and markdown formatting."
                )
                return

            # Calculate readability
            score = calculate_readability(plain_text)
            complex_sentences = get_complex_sentences(plain_text, threshold=12.0)

            # Display results
            self.display_results(score, complex_sentences)

        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {self.selected_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

    def display_results(self, score, complex_sentences):
        """Display the analysis results."""
        # Update score
        self.score_label.config(text=f"{score}")

        # Set color based on score
        if score <= 8:
            color = "#2e7d32"  # Green
        elif score <= 12:
            color = "#f57c00"  # Orange
        else:
            color = "#c62828"  # Red
        self.score_label.config(foreground=color)

        # Update interpretation
        interpretation = self.get_interpretation(score)
        self.interpretation_label.config(text=interpretation)

        # Update complex sentences display
        self.results_text.config(state="normal")
        self.results_text.delete(1.0, tk.END)

        if complex_sentences:
            for i, sentence in enumerate(complex_sentences, 1):
                self.results_text.insert(tk.END, f"• {sentence}\n\n", "bullet")
        else:
            self.results_text.insert(
                tk.END,
                "No complex sentences found. All sentences are at grade level 12 or below.",
                "none"
            )

        self.results_text.config(state="disabled")

    def get_interpretation(self, score):
        """Get text interpretation of grade level score."""
        if score <= 6:
            return "(Elementary school level)"
        elif score <= 8:
            return "(Middle school level)"
        elif score <= 12:
            return "(High school level)"
        elif score <= 16:
            return "(College level)"
        else:
            return "(Graduate school level)"


def main():
    """Launch the GUI application."""
    root = tk.Tk()
    app = ReadabilityCalculatorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
