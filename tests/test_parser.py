import os
from pathlib import Path
from models.parser import save_processed_text


def test_pdf_parsing():
    project_root = Path(__file__).parent.parent
    input_file = project_root / "data" / "sample_notes" / "docs.pdf"

    output_file = save_processed_text(str(input_file))

    # Check if output file is created
    assert os.path.exists(output_file), f"Processed text file not created: {output_file}"

    # Check if the content is not empty
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert len(content) > 0, "Extracted text is empty"
