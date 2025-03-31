import os
import logging
import json
import argparse
from word_parser import parse_word
from pdf_parser import parse_pdf
from txt_parser import parse_txt
from mcq_formatter import format_mcq_data
from ppt_generator import generate_ppt
from latex_generator import generate_latex

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_file(file_name, input_dir, output_dir):
    input_path = os.path.join(input_dir, file_name)
    output_path_ppt = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.pptx")
    output_path_latex = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}")

    if file_name.endswith(".docx"):
        logging.info(f"Processing Word file: {file_name}")
        raw_data = parse_word(input_path)
    elif file_name.endswith(".pdf"):
        logging.info(f"Processing PDF file: {file_name}")
        raw_data = parse_pdf(input_path)
    elif file_name.endswith(".txt"):
        logging.info(f"Processing Text file: {file_name}")
        raw_data = parse_txt(input_path)
    else:
        logging.warning(f"Skipping unsupported file format: {file_name}")
        return

    mcq_data = format_mcq_data(raw_data)
    logging.info(f"Formatted MCQ Data: {mcq_data}")

    generate_ppt(mcq_data, output_path_ppt)
    logging.info(f"Generated PPT: {output_path_ppt}")

    generate_latex(mcq_data, output_path_latex)
    logging.info(f"Generated LaTeX: {output_path_latex}.pdf")

def main():
    parser = argparse.ArgumentParser(description="Process MCQ files and generate outputs.")
    parser.add_argument("--input_dir", type=str, default="../input_files", help="Path to the input directory")
    parser.add_argument("--output_dir", type=str, default="../output_files", help="Path to the output directory")
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        try:
            process_file(file_name, input_dir, output_dir)
        except Exception as e:
            logging.error(f"Error processing file {file_name}: {e}")

if __name__ == "__main__":
    main()