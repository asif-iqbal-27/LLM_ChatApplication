import os
from PyPDF2 import PdfReader

EXTRACTED_TEXT_DIR = "data/extracted_texts/"
os.makedirs(EXTRACTED_TEXT_DIR, exist_ok=True)

def extract_text_from_all_pdfs(pdf_folder: str):
    """Extracts text from all PDFs in the given folder and saves them as text files."""
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    extracted_files = {}

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        reader = PdfReader(pdf_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        
        # Define extracted text filename
        text_filename = pdf_file.replace(".pdf", ".txt")
        output_path = os.path.join(EXTRACTED_TEXT_DIR, text_filename)
        
        # Save extracted text
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        
        extracted_files[pdf_file] = output_path

    return extracted_files  # Return dictionary of PDF file names and their extracted text paths
pdf_folder = "data/pdfs/"  # Path where all PDFs are stored
extracted_files = extract_text_from_all_pdfs(pdf_folder)

for pdf, txt in extracted_files.items():
    print(f"Extracted text for {pdf} saved in: {txt}")