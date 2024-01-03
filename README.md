# Password Generator

This is a password generator application written in Python. It uses the PyQt5 library for the user interface and the secrets library for generating cryptographically secure random passwords.

## Features

- Responsive interface that works well on different screen sizes.
- Error handling for scenarios like invalid input or password generation failure.
- A visual indicator of password strength based on the generated password's complexity (optional enhancement).
- A section to display the history of generated passwords (optional enhancement).
- Settings persistence to save preferred settings (optional enhancement).
- Unit tests for the password generation logic to ensure its correctness (optional enhancement).

## Dependencies

This project uses the following libraries:

- PyQt5
- secrets
- pyperclip
- secrets
- string

You can install them using pip:
```bash
pip install PyQt5 pyperclip secrets string
```

## Installation

Clone the repository and run the main.py file.

```bash
git clone https://github.com/Kaanhehe/Password-Manager
cd Password-Manager
python main.py
```