import os
import PyPDF2
import docx

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file"""
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX file"""
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def save_processed_text(input_path: str, output_dir: str = "data/processed") -> str:
    """Extract and save text from PDF/DOCX into processed folder"""
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.splitext(os.path.basename(input_path))[0] + ".txt"
    output_path = os.path.join(output_dir, filename)

    if input_path.endswith(".pdf"):
        text = extract_text_from_pdf(input_path)
    elif input_path.endswith(".docx"):
        text = extract_text_from_docx(input_path)
    else:
        raise ValueError("Unsupported file format")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return output_path
