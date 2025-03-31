import os
from docx import Document

def parse_word(file_path):
    """
    Parse a Word document to extract text and images.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Word file not found: {file_path}")

    doc = Document(file_path)
    mcq_data = {"questions": [], "images": []}

    # Extract text from paragraphs
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            mcq_data["questions"].append(paragraph.text.strip())

    # Extract images (if any)
    for i, rel in enumerate(doc.part.rels.values()):
        if "image" in rel.target_ref:
            image_data = rel.target_part.blob
            image_path = f"../output_files/image_{i + 1}.png"
            with open(image_path, "wb") as img_file:
                img_file.write(image_data)
            mcq_data["images"].append(image_path)

    return mcq_data