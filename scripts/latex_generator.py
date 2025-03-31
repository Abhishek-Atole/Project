from pylatex import Document, Section, Subsection, Command, NoEscape
from pylatex.utils import italic, bold

def generate_latex(mcq_data, output_path):
    """
    Generate a LaTeX document from MCQ data.
    """
    from pylatex import Document, Section, Subsection, Command, NoEscape
    from pylatex.utils import bold

    doc = Document()

    # Add a title
    doc.preamble.append(Command('title', 'MCQ Questions'))
    doc.preamble.append(Command('author', 'Auto-Generated'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    # Add MCQ questions
    with doc.create(Section('Multiple Choice Questions')):
        for question_data in mcq_data["questions"]:
            # Add the question
            doc.append(bold(f"Q: {question_data['question']}"))
            doc.append("\n")

            # Add the choices as a bullet list
            with doc.create(Subsection('Choices')):
                for choice in question_data["choices"]:
                    doc.append(f"- {choice}\n")

            # Add equations if the question contains one
            if "x^2" in question_data["question"]:  # Example condition
                doc.append(NoEscape(r'\begin{equation}'))
                doc.append(NoEscape(r'x^2 - 4 = 0'))
                doc.append(NoEscape(r'\end{equation}'))

            # Add images if available
            if question_data["images"]:
                for image_path in question_data["images"]:
                    doc.append(NoEscape(r'\includegraphics[width=0.5\textwidth]{' + image_path + '}'))
                    doc.append("\n")

    # Save the LaTeX document
    doc.generate_pdf(output_path, clean_tex=False)
    print(f"LaTeX document saved at: {output_path}.pdf")