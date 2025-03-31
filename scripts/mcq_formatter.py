def format_mcq_data(raw_data):
    """
    Format raw extracted data into structured MCQ format.
    """
    formatted_data = {"questions": []}

    for i, question_text in enumerate(raw_data["questions"]):
        # Example logic to split question and choices
        parts = question_text.split("\n")
        question = parts[0]  # First line is the question
        choices = parts[1:]  # Remaining lines are choices

        # Add question, choices, and associated images
        formatted_data["questions"].append({
            "question": question,
            "choices": choices,
            "images": raw_data["images"][i:i+1] if i < len(raw_data["images"]) else []
        })

    return formatted_data