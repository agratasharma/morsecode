# Morse Code Translator

A Python application for encoding and decoding Morse code, with both command-line and web interfaces.

## Features

- Encode text to Morse code
- Decode Morse code to text
- Web interface using Flask
- Unit tests with automatic CI

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/agratasharma/morsecode.git
   cd morsecode
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line

Run the encoder/decoder directly:
```bash
python encoder_decoder.py
```

### Web Server

Start the Flask web server:
```bash
python app.py
```

Then open http://localhost:5000 in your browser.

### Running Tests

Run unit tests locally:
```bash
python -m unittest test_encoderdecoder.py
```

## Git Workflow

- **Main Branch**: Protected, requires passing CI
- **CI Pipeline**: Runs unit tests on every push to main
- **Pull Requests**: Create PRs for new features, tests will run automatically

## Project Structure

- `encoder_decoder.py`: Core encoding/decoding functions
- `morse_translator.py`: Class wrapper for the functions
- `app.py`: Flask web application
- `test_encoderdecoder.py`: Unit tests
- `.github/workflows/ci.yml`: GitHub Actions CI configuration