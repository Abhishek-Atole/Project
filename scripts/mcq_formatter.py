def format_mcq_data(raw_data):
    """
    Format raw extracted data into structured MCQ format.
    """
    formatted_data = {"questions": []}

    question = None
    choices = []

    for line in raw_data["questions"]:
        line = line.strip()
        if not line:
            continue

        # Detect a new question
        if line.endswith("?") or line.startswith("Solve"):
            # Save the previous question and its choices
            if question:
                formatted_data["questions"].append({
                    "question": question,
                    "choices": choices,
                    "images": []
                })
            # Start a new question
            question = line
            choices = []
        else:
            # Add to choices
            choices.append(line)

    # Add the last question
    if question:
        formatted_data["questions"].append({
            "question": question,
            "choices": choices,
            "images": []
        })

    return formatted_data