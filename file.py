import os

def create_project_structure(base_path="."):
    # Define the directory structure
    directories = [
        "input_files",
        "output_files",
        "scripts"
    ]
    
    script_files = {
        "scripts/main.py": "# Main script to run the project\n",
        "scripts/word_parser.py": "# Script to handle Word file parsing\n",
        "scripts/pdf_parser.py": "# Script to handle PDF file parsing\n",
        "scripts/ppt_generator.py": "# Script to generate PowerPoint presentations\n",
        "scripts/utils.py": "# Utility functions (e.g., OCR, image processing)\n"
    }
    
    other_files = {
        "requirements.txt": "# Python dependencies\n",
        "README.md": "# Project documentation\n"
    }
    
    # Create directories
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
    
    # Create script files with placeholders
    for file_path, content in script_files.items():
        full_path = os.path.join(base_path, file_path)
        with open(full_path, "w") as f:
            f.write(content)
    
    # Create other files
    for file_path, content in other_files.items():
        full_path = os.path.join(base_path, file_path)
        with open(full_path, "w") as f:
            f.write(content)
    
    print(f"Project structure created at: {os.path.abspath(base_path)}")

if __name__ == "__main__":
    create_project_structure()