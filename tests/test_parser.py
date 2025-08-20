import os
from models.parser import save_processed_text

def test_pdf_parsing():

    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert len(content) > 0, "Extracted text is empty"
