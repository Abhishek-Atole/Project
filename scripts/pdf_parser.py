from PyPDF2 import PdfReader

def parse_pdf(file_path):
    """
    Parse a PDF file to extract text and images.
    """
    reader = PdfReader(file_path)
    mcq_data = {"questions": []}

    # Extract text from PDF pages
    for page in reader.pages:
        text = page.extract_text()
        if text:
            mcq_data["questions"].extend(text.split("\n"))

    return mcq_data