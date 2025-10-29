import math
import os
import sys
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# --- Rich UI Library Imports ---
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress

# --- Core Logic (No Changes Here) ---

def calculate_entropy(text):
    """Calculates the Shannon entropy of a given text."""
    text = text.replace('\n', '')
    text_length = len(text)
    if text_length == 0:
        return 0
    char_counts = Counter(text)
    entropy = 0.0
    for count in char_counts.values():
        probability = count / text_length
        entropy -= probability * math.log2(probability)
    return entropy

def plot_char_distribution(text, top_n=30, filename='character_distribution.png'):
    """Plots the distribution of the most common characters and saves it."""
    text_for_plot = text.replace('\n', '')
    char_counts = Counter(text_for_plot)
    common_chars = char_counts.most_common(top_n)
    characters, counts = zip(*common_chars)
    
    plt.figure(figsize=(15, 7))
    plt.bar(characters, counts, color='deepskyblue')
    plt.title(f'Top {top_n} Most Frequent Characters in Password File')
    plt.xlabel('Character')
    plt.ylabel('Frequency (Count)')
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# --- MAIN FUNCTION (Updated with Rich UI) ---

def main():
    """Main function to run the analysis and display a rich UI."""
    
    # --- Setup ---
    console = Console()
    password_filename = 'rockyou.txt' 
    
    console.print(Panel.fit("[bold magenta]Password Entropy Analyzer 🔑[/bold magenta]", 
                            subtitle="A quantitative analysis of password strength"))

    # --- Data Sourcing with Progress Bar ---
    password_data = ""
    try:
        file_size = os.path.getsize(password_filename)
        with Progress(console=console) as progress:
            task = progress.add_task(f"[cyan]Reading '{password_filename}'...", total=file_size)
            with open(password_filename, 'r', encoding='latin-1') as f:
                while chunk := f.read(4096): # Read in 4KB chunks
                    password_data += chunk
                    progress.update(task, advance=len(chunk.encode('latin-1')))
    except FileNotFoundError:
        console.print(f"\n[bold red]Error:[/bold red] The file '{password_filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] An unexpected error occurred: {e}")
        sys.exit(1)

    # --- Analysis ---
    console.print("\n[yellow]Performing mathematical analysis...[/yellow]")
    final_entropy = calculate_entropy(password_data)
    total_chars = len(password_data.replace('\n',''))
    unique_chars = len(Counter(password_data.replace('\n','')))

    # --- Display Results in a Table ---
    table = Table(title="📊 Analysis Results", show_header=True, header_style="bold blue")
    table.add_column("Metric", style="dim", width=30)
    table.add_column("Value", style="bold")

    table.add_row("Analyzed File", password_filename)
    table.add_row("Total Characters Analyzed", f"{total_chars:,}")
    table.add_row("Unique Characters Found", str(unique_chars))
    table.add_row("[cyan]Final Shannon Entropy[/cyan]", f"{final_entropy:.4f} bits per character")

    console.print(table)
    
    # --- Visualization ---
    console.print("\n[yellow]Generating character frequency plot...[/yellow]")
    plot_char_distribution(password_data)
    
    console.print("\n[bold green]✅ Process complete.[/bold green]")


if __name__ == "__main__":
    main()