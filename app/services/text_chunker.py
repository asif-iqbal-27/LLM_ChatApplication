import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

CHUNKED_TEXT_DIR = "data/chunked_texts/"
os.makedirs(CHUNKED_TEXT_DIR, exist_ok=True)

def chunk_text(file_path: str, chunk_size: int = 1000, chunk_overlap: int = 200):
    """Reads extracted text from a file, chunks it, and saves as a .txt file."""

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )

    chunks = text_splitter.split_text(text)

    # Define the chunked text filename
    chunked_file_path = os.path.join(CHUNKED_TEXT_DIR, os.path.basename(file_path).replace(".txt", "_chunked.txt"))

    # Save each chunk in a new line in the .txt file
    with open(chunked_file_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n\n")  # Separate chunks with a new line

    return chunked_file_path  # Return saved chunked text file path

def chunk_all_extracted_texts():
    """Processes all extracted text files and chunks them."""
    extracted_text_dir = "data/extracted_texts/"
    extracted_files = [f for f in os.listdir(extracted_text_dir) if f.endswith(".txt")]
    
    chunked_files = {}
    for text_file in extracted_files:
        text_path = os.path.join(extracted_text_dir, text_file)
        chunked_file = chunk_text(text_path)
        chunked_files[text_file] = chunked_file
    
    return chunked_files  # Return dictionary of extracted text filenames and chunked text file paths


chunked_files = chunk_all_extracted_texts()

for original, chunked in chunked_files.items():
    print(f"Chunked text for {original} saved in: {chunked}")
