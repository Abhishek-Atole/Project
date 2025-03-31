import sys
import os
print(sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
from word_parser import parse_word

def parse_txt(file_path):
    """
    Parse a plain text file to extract questions, choices, and images.
    """
    mcq_data = {"questions": []}

    try:
        with open(file_path, "r") as file:
            # Add logic to parse the text file
            pass
    except Exception as e:
        raise RuntimeError(f"Error parsing text file {file_path}: {e}")