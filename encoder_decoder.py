#STAGE1
# morse_magic_stage1.py

# Dictionary: English characters to Morse code
MORSE_CODE = {
    "A": ".-",     "B": "-...",   "C": "-.-.",   "D": "-..",
    "E": ".",      "F": "..-.",   "G": "--.",    "H": "....",
    "I": "..",     "J": ".---",   "K": "-.-",    "L": ".-..",
    "M": "--",     "N": "-.",     "O": "---",    "P": ".--.",
    "Q": "--.-",   "R": ".-.",    "S": "...",    "T": "-",
    "U": "..-",    "V": "...-",   "W": ".--",    "X": "-..-",
    "Y": "-.--",   "Z": "--..",

    "0": "-----",  "1": ".----",  "2": "..---",  "3": "...--",
    "4": "....-",  "5": ".....",  "6": "-....",  "7": "--...",
    "8": "---..",  "9": "----.",

    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.",  "(": "-.--.",  ")": "-.--.-",
    "&": ".-...",  ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.",  "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-."
}

# Reverse dictionary: Morse code to English characters
TEXT_CODE = {value: key for key, value in MORSE_CODE.items()}


def encode_to_morse(text):
    """
    Converts normal text into Morse code.
    Letters are separated by spaces.
    Words are separated by /.
    """
    if not text.strip():
        return "Error: Please enter some text."

    morse_message = []

    for char in text.upper():
        if char == " ":
            morse_message.append("/")
        elif char in MORSE_CODE:
            morse_message.append(MORSE_CODE[char])
        else:
            return f"Error: Unsupported character found: {char}"

    return " ".join(morse_message)


def decode_from_morse(morse):
    """
    Converts Morse code back into normal text.
    Morse letters should be separated by spaces.
    Words should be separated by /.
    """
    if not morse.strip():
        return "Error: Please enter Morse code."

    words = morse.strip().split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_word = ""

        for symbol in letters:
            if symbol in TEXT_CODE:
                decoded_word += TEXT_CODE[symbol]
            else:
                return f"Error: Invalid Morse code found: {symbol}"

        decoded_words.append(decoded_word)

    return " ".join(decoded_words)


def main():
    print("Welcome to Morse Magic - Stage 1")
    print("1. Encode text to Morse")
    print("2. Decode Morse to text")

    choice = input("Choose option 1 or 2: ")

    if choice == "1":
        text = input("Enter text: ")
        print("Morse Code:")
        print(encode_to_morse(text))

    elif choice == "2":
        morse = input("Enter Morse code: ")
        print("Decoded Text:")
        print(decode_from_morse(morse))

    else:
        print("Error: Invalid choice.")


if __name__ == "__main__":
    main()