import ctypes
import os

# Load the shared library
lib = ctypes.CDLL("./image_preprocessor.so")

def preprocess_image(input_path, output_path):
    """
    Preprocess an image using the C++ shared library.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Call the C++ function
    lib.preprocess_image(input_path.encode('utf-8'), output_path.encode('utf-8'))
    print(f"Image processed and saved to: {output_path}")