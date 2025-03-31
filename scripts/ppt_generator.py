from pptx import Presentation

def generate_ppt(mcq_data, output_path):
    """
    Generate a PowerPoint presentation from MCQ data.
    """
    prs = Presentation()

    for question in mcq_data["questions"]:
        slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title and Content layout
        slide.shapes.title.text = "Question"
        slide.placeholders[1].text = question

    prs.save(output_path)