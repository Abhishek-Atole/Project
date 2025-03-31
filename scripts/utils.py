import cv2
import pytesseract
import requests
import os

def preprocess_image(image_path):
    """
    Preprocess an image for better OCR accuracy.
    - Convert to grayscale.
    - Apply thresholding.
    - Remove noise.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Apply thresholding
    _, processed_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Optional: Apply GaussianBlur to reduce noise
    processed_image = cv2.GaussianBlur(processed_image, (5, 5), 0)

    return processed_image

def extract_text_from_image(image_path):
    """
    Extract text from an image using Tesseract OCR.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    text = pytesseract.image_to_string(image)
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