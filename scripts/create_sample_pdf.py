from fpdf import FPDF

def create_sample_pdf(file_path):
    """
    Create a sample PDF document with questions and choices.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add a title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Sample MCQ Questions", ln=True, align="C")
    pdf.ln(10)

    # Add a question with choices
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="What is 2 + 2?", ln=True)
    pdf.cell(200, 10, txt="A. 3", ln=True)
    pdf.cell(200, 10, txt="B. 4", ln=True)
    pdf.cell(200, 10, txt="C. 5", ln=True)
    pdf.cell(200, 10, txt="D. 6", ln=True)
    pdf.ln(10)

    # Add another question
    pdf.cell(200, 10, txt="Solve the equation: x^2 - 4 = 0", ln=True)
    pdf.cell(200, 10, txt="A. x = 2", ln=True)
    pdf.cell(200, 10, txt="B. x = -2", ln=True)
    pdf.cell(200, 10, txt="C. x = ±2", ln=True)
    pdf.cell(200, 10, txt="D. None", ln=True)

    # Save the PDF
    pdf.output(file_path)
    print(f"Sample PDF document created at: {file_path}")

# Generate the file in the input_files directory
create_sample_pdf("../input_files/sample.pdf")