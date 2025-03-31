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
