import unittest
from morse_translator import MorseCodeTranslator


class TestMorseCodeTranslator(unittest.TestCase):

    def setUp(self):
        self.translator = MorseCodeTranslator()

    def test_encode_single_word(self):
        self.assertEqual(
            self.translator.encode("HELLO"),
            ".... . .-.. .-.. ---"
        )

    def test_encode_sentence(self):
        self.assertEqual(
            self.translator.encode("HELLO WORLD"),
            ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        )

    def test_encode_lowercase(self):
        self.assertEqual(
            self.translator.encode("hello"),
            ".... . .-.. .-.. ---"
        )

    def test_encode_empty_input(self):
        self.assertEqual(
            self.translator.encode(""),
            "Error: Please enter some text."
        )

    def test_encode_invalid_character(self):
        self.assertEqual(
            self.translator.encode("HELLO #"),
            "Error: Unsupported character found: #"
        )

    def test_decode_single_word(self):
        self.assertEqual(
            self.translator.decode(".... . .-.. .-.. ---"),
            "HELLO"
        )

    def test_decode_sentence(self):
        self.assertEqual(
            self.translator.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
            "HELLO WORLD"
        )

    def test_decode_empty_input(self):
        self.assertEqual(
            self.translator.decode(""),
            "Error: Please enter Morse code."
        )

    def test_decode_invalid_morse(self):
        self.assertEqual(
            self.translator.decode(".... invalid"),
            "Error: Invalid Morse code found: invalid"
        )


if __name__ == "__main__":
    unittest.main()
    