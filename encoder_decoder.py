class MorseCodeTranslator:
    """
    A class to encode text into Morse code and decode Morse code into text.
    """

    MORSE_CODE = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",

        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",

        ".": ".-.-.-", ",": "--..--", "?": "..--..",
        "!": "-.-.--", "/": "-..-.", "-": "-....-",
        "@": ".--.-."
    }

    def __init__(self):
        self.text_code = {value: key for key, value in self.MORSE_CODE.items()}

    def encode(self, text):
        if not text.strip():
            return "Error: Please enter some text."

        encoded_message = []

        for char in text.upper():
            if char == " ":
                encoded_message.append("/")
            elif char in self.MORSE_CODE:
                encoded_message.append(self.MORSE_CODE[char])
            else:
                return f"Error: Unsupported character found: {char}"

        return " ".join(encoded_message)

    def decode(self, morse):
        if not morse.strip():
            return "Error: Please enter Morse code."

        words = morse.strip().split(" / ")
        decoded_words = []

        for word in words:
            decoded_word = ""

            for symbol in word.split():
                if symbol in self.text_code:
                    decoded_word += self.text_code[symbol]
                else:
                    return f"Error: Invalid Morse code found: {symbol}"

            decoded_words.append(decoded_word)

        return " ".join(decoded_words)


def main():
    translator = MorseCodeTranslator()

    print("Welcome to Morse Magic - Stage 2")
    print("1. Encode text to Morse")
    print("2. Decode Morse to text")

    choice = input("Choose option 1 or 2: ")

    if choice == "1":
        text = input("Enter text: ")
        print(translator.encode(text))

    elif choice == "2":
        morse = input("Enter Morse code: ")
        print(translator.decode(morse))

    else:
        print("Error: Invalid choice.")


if __name__ == "__main__":
    main()