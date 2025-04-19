import os
from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog

def select_pdfs():
    """Show a file picker to choose multiple PDF files."""
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(
        title="Select PDFs to merge",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return list(files)

def merge_pdfs(pdf_paths, output_path):
    """Merge a list of PDFs into a single file at `output_path`."""
    merger = PdfMerger()
    for path in pdf_paths:
        merger.append(path)
    merger.write(output_path)
    merger.close()
    print(f"[✓] Merged {len(pdf_paths)} files into: {output_path}")

if __name__ == "__main__":
    pdf_files = select_pdfs()
    if not pdf_files:
        print("❌ No PDFs selected – exiting.")
        exit(0)

    output_name = input("Enter output filename (e.g. combined.pdf): ").strip()
    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    merge_pdfs(pdf_files, output_name)
