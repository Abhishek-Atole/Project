def parse_txt(file_path):
    """
    Parse a plain text file to extract questions, choices, and images.
    """
    mcq_data = {"questions": []}

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        question = None
        choices = []
        images = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Detect an image line
            if line.startswith("image:"):
                image_path = line.split("image:")[1].strip()
                images.append(image_path)
                continue

            # Detect a new question
            if line.endswith("?"):
                # Save the previous question and its choices
                if question:
                    if not choices:
                        raise ValueError(f"Missing choices for question: {question}")
                    mcq_data["questions"].append({
                        "question": question,
                        "choices": choices,
                        "images": images
                    })
                # Start a new question
                question = line
                choices = []
                images = []
            else:
                # Add to choices
                choices.append(line)

        # Add the last question
        if question:
            if not choices:
                raise ValueError(f"Missing choices for question: {question}")
            mcq_data["questions"].append({
                "question": question,
                "choices": choices,
                "images": images
            })

    except Exception as e:
        print(f"Error parsing text file {file_path}: {e}")

    return mcq_data