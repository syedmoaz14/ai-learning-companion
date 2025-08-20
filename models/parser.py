import os
from pathlib import Path
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
    """
    Extract and save text from PDF/DOCX into the project-level processed folder.
    Always resolves paths relative to the project root.
    """
    project_root = Path(__file__).parent.parent  # repo root (where your project starts)
    output_dir = project_root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = Path(input_path).stem + ".txt"
    output_path = output_dir / filename

    if input_path.endswith(".pdf"):
        text = extract_text_from_pdf(input_path)
    elif input_path.endswith(".docx"):
        text = extract_text_from_docx(input_path)
    else:
        raise ValueError("Unsupported file format")

    output_path.write_text(text, encoding="utf-8")

    print(f"[INFO] Processed file saved at: {output_path}")  # helpful debug log
    return str(output_path)
