import os
from models.parser import save_processed_text

def test_pdf_parsing():
    input_file = "data/sample_notes/sample.pdf"  # put a sample file here
    output_file = save_processed_text(input_file)

    assert os.path.exists(output_file), "Processed text file not created"
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert len(content) > 0, "Extracted text is empty"
