import unittest

from encoder_decoder import encode_to_morse, decode_from_morse


class TestMorseMagicStage1(unittest.TestCase):

    # Encoding tests
    def test_encode_single_word(self):
        self.assertEqual(
            encode_to_morse("HELLO"),
            ".... . .-.. .-.. ---"
        )

    def test_encode_sentence_with_space(self):
        self.assertEqual(
            encode_to_morse("HELLO WORLD"),
            ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        )

    def test_encode_lowercase_text(self):
        self.assertEqual(
            encode_to_morse("hello"),
            ".... . .-.. .-.. ---"
        )

    def test_encode_numbers(self):
        self.assertEqual(
            encode_to_morse("123"),
            ".---- ..--- ...--"
        )

    def test_encode_empty_input(self):
        self.assertEqual(
            encode_to_morse(""),
            "Error: Please enter some text."
        )

    def test_encode_unsupported_character(self):
        self.assertEqual(
            encode_to_morse("Hello #"),
            "Error: Unsupported character found: #"
        )

    # Decoding tests
    def test_decode_single_word(self):
        self.assertEqual(
            decode_from_morse(".... . .-.. .-.. ---"),
            "HELLO"
        )

    def test_decode_sentence_with_space(self):
        self.assertEqual(
            decode_from_morse(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
            "HELLO WORLD"
        )

    def test_decode_numbers(self):
        self.assertEqual(
            decode_from_morse(".---- ..--- ...--"),
            "123"
        )

    def test_decode_empty_input(self):
        self.assertEqual(
            decode_from_morse(""),
            "Error: Please enter Morse code."
        )

    def test_decode_invalid_morse(self):
        self.assertEqual(
            decode_from_morse(".... . invalid"),
            "Error: Invalid Morse code found: invalid"
        )


if __name__ == "__main__":
    unittest.main()