from ppt_generator import generate_ppt

# Sample MCQ data
mcq_data = {
    "questions": [
        {
            "question": "What is 2 + 2?",
            "choices": ["A. 3", "B. 4", "C. 5", "D. 6"],
            "images": []
        },
        {
            "question": "Solve the equation: x^2 - 4 = 0",
            "choices": ["A. x = 2", "B. x = -2", "C. x = ±2", "D. None"],
            "images": []
        }
    ]
}

# Test output path
output_path = "../output_files/test_output.pptx"

# Generate PowerPoint
generate_ppt(mcq_data, output_path)