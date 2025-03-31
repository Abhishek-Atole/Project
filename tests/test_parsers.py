import unittest
from parsers import parse_word

class TestParsers(unittest.TestCase):
    def test_parse_word(self):
        import pdb; pdb.set_trace()
        result = parse_word("test_files/sample.docx")
        self.assertIn("What is 2 + 2?", result["questions"][0]["question"])

if __name__ == "__main__":
    unittest.main()