import os
from word_parser import parse_word
from pdf_parser import parse_pdf
from mcq_formatter import format_mcq_data
from ppt_generator import generate_ppt
from latex_generator import generate_latex

def main():
    # Input and output directories
    input_dir = "../input_files"
    output_dir = "../output_files"
    os.makedirs(output_dir, exist_ok=True)

    # Process each file in the input directory
    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)
        output_path_ppt = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.pptx")
        output_path_latex = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}")

        # Skip unsupported file formats
        if not (file_name.endswith(".docx") or file_name.endswith(".pdf")):
            print(f"Skipping unsupported file format: {file_name}")
            continue

        if file_name.endswith(".docx"):
            print(f"Processing Word file: {file_name}")
            raw_data = parse_word(input_path)
        elif file_name.endswith(".pdf"):
            print(f"Processing PDF file: {file_name}")
            raw_data = parse_pdf(input_path)

        mcq_data = format_mcq_data(raw_data)
        print("Formatted MCQ Data:", mcq_data)

        # Generate PowerPoint presentation
        generate_ppt(mcq_data, output_path_ppt)
        print(f"Generated PPT: {output_path_ppt}")

        # Generate LaTeX document
        generate_latex(mcq_data, output_path_latex)
        print(f"Generated LaTeX: {output_path_latex}.pdf")

if __name__ == "__main__":
    main()