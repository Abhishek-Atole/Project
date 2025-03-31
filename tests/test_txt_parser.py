import unittest
from txt_parser import parse_txt

class TestTxtParser(unittest.TestCase):
    def test_parse_txt_valid(self):
        # Sample input
        sample_text = """What is the capital of France?
        A. Berlin
        B. Madrid
        C. Paris
        D. Rome
        """
        with open("sample.txt", "w") as f:
            f.write(sample_text)

        # Parse the file
        result = parse_txt("sample.txt")

        # Print processed image data (sample)
        print("Processed image data (sample):")
        print(result[:5, :5])  # Print the top-left 5x5 portion of the array

        # Expected output
        expected = {
            "questions": [
                {
                    "question": "What is the capital of France?",
                    "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
                    "images": []
                }
            ]
        }

        self.assertEqual(result, expected)

    def test_parse_txt_missing_choices(self):
        # Sample input with missing choices
        sample_text = """What is the capital of France?"""
        with open("sample.txt", "w") as f:
            f.write(sample_text)

        # Parse the file and expect an error
        with self.assertRaises(ValueError):
            parse_txt("sample.txt")

if __name__ == "__main__":
    unittest.main()