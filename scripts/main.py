import os
from word_parser import parse_word
from pdf_parser import parse_pdf
from mcq_formatter import format_mcq_data
from ppt_generator import generate_ppt

def main():
    # Input and output directories
    input_dir = "../input_files"
    output_dir = "../output_files"
    os.makedirs(output_dir, exist_ok=True)

    # Process each file in the input directory
    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)

        # Generate unique output file names
        if file_name.endswith(".docx"):
            output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_word.pptx")
        elif file_name.endswith(".pdf"):
            output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_pdf.pptx")
        else:
            print(f"Skipping unsupported file format: {file_name}")
            continue

        # Process the file and generate the PowerPoint
        if file_name.endswith(".docx"):
            print(f"Processing Word file: {file_name}")
            raw_data = parse_word(input_path)
        elif file_name.endswith(".pdf"):
            print(f"Processing PDF file: {file_name}")
            raw_data = parse_pdf(input_path)

        mcq_data = format_mcq_data(raw_data)
        print("Formatted MCQ Data:", mcq_data)
        generate_ppt(mcq_data, output_path)
        print(f"Generated PPT: {output_path}")

if __name__ == "__main__":
    main()