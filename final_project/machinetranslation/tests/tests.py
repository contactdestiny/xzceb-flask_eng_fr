import unittest
from translator import english_to_french, french_to_english

class TestsEnglishFrench(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(english_to_french("No null value"), True)
        # self.assertIsNotNone(french_to_english(None), False)
        self.assertIsNotNone(french_to_english("No null value"), True)

    def test2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()