import pytesseract
from PyPDF2 import PdfReader
import cv2
import os

def parse_pdf(file_path):
    """
    Parse a PDF file to extract text, images, and equations.
    """
    reader = PdfReader(file_path)
    mcq_data = {"questions": [], "images": []}

    # Extract text from PDF pages
    for page in reader.pages:
        text = page.extract_text()
        if text:
            mcq_data["questions"].append(text.strip())

    # Extract images from PDF (if any)
    for i, page in enumerate(reader.pages):
        if "/XObject" in page["/Resources"]:
            xObject = page["/Resources"]["/XObject"].get_object()
            for obj in xObject:
                if xObject[obj]["/Subtype"] == "/Image":
                    size = (xObject[obj]["/Width"], xObject[obj]["/Height"])
                    data = xObject[obj].get_data()
                    image_path = f"../output_files/pdf_image_{i + 1}.png"
                    with open(image_path, "wb") as img_file:
                        img_file.write(data)
                    mcq_data["images"].append(image_path)

    return mcq_data