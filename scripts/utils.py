import cv2
import pytesseract
import requests
import os
from image_preprocessor import preprocess_image

def extract_text_from_image(image_path, processed_path):
    """
    Extract text from an image using Tesseract OCR after preprocessing.
    """
    # Preprocess the image
    preprocess_image(image_path, processed_path)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(processed_path)
    return text

def extract_equation_with_mathpix(image_path, app_id, app_key):
    """
    Extract mathematical equations from an image using MathPix API.
    Requires MathPix App ID and App Key.
    """
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    headers = {
        "app_id": app_id,
        "app_key": app_key,
        "Content-type": "application/json",
    }

    data = {
        "src": f"data:image/png;base64,{image_data.decode('latin1')}",
        "formats": ["text", "latex"],
    }

    response = requests.post("https://api.mathpix.com/v3/text", json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("latex", "")
    else:
        print(f"MathPix API Error: {response.status_code}")
        return ""