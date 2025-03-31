# MCQ Processing Application

## Overview
This application processes various input files (Word, PDF, text, and images) to extract MCQs, format them, and generate outputs in PowerPoint and LaTeX formats.

## Features
- Extracts text and MCQs from `.docx`, `.pdf`, `.txt`, and image files.
- Preprocesses images for OCR using OpenCV and Pybind11.
- Generates PowerPoint presentations and LaTeX documents.

## Requirements
- Python 3.12+
- Required Python packages:
  - `opencv-python`
  - `pytesseract`
  - `pybind11`
- OpenCV installed on the system.

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Project
   ```

## Project Structure
```
Project/
├── input_files/
├── output_files/
├── logs/
├── scripts/
│   ├── main.py
│   ├── word_parser.py
│   ├── pdf_parser.py
│   ├── txt_parser.py
│   ├── mcq_formatter.py
│   ├── ppt_generator.py
│   ├── latex_generator.py
│   ├── image_preprocessor.cpp
│   ├── image_preprocessor.cpython-<version>.so
├── tests/
│   ├── test_parsers.py
│   ├── test_image_preprocessor.py
├── [requirements.txt](http://_vscodecontentref_/2)
├── [README.md](http://_vscodecontentref_/3)
└── LICENSE
```

---
### **Steps to Add the README File**
1. Create a new file named [README.md](http://_vscodecontentref_/4) in the root of your project:
   ```bash
   touch README.md
