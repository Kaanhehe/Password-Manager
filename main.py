#Password Generator with Tkinter
#Features:
#User Interface:
#
#Use Tkinter, a standard GUI toolkit for Python, to create a graphical interface.
#Include input fields for password length and checkboxes for including/excluding numbers, symbols, uppercase, and lowercase letters.
#Display the generated password in a text box.
#Add a "Copy to Clipboard" button to easily copy the generated password.
#Password Generation Logic:
#
#Implement a password generation function that takes user preferences into account.
#Use the secrets module to generate cryptographically secure random numbers.
#Combine characters based on user preferences and generate the final password.
#User Preferences:
#
#Allow users to specify the length of the password.
#Include checkboxes or toggle buttons for:
#Include numbers (0-9)
#Include symbols (!@#$%^&*)
#Include uppercase letters (A-Z)
#Include lowercase letters (a-z)
#Copy to Clipboard:
#
#Utilize the pyperclip module to copy the generated password to the clipboard.
#Provide a visual indication or a popup message confirming the successful copy.
#Clean and Responsive Design:
#
#Create a clean and user-friendly design for the GUI.
#Ensure that the interface is responsive and works well on different screen sizes.
#Error Handling:
#
#Implement error handling to manage scenarios like invalid input or password generation failure.
#Provide informative messages to guide the user in case of errors.
#README File:
#
#Write a comprehensive README file that explains the project, its features, and how to use it.
#Include any dependencies and installation instructions.
#Code Comments and Documentation:
#
#Add comments in your code to explain complex logic or functionality.
#Consider writing a brief documentation to help other developers understand your code.
#Optional Enhancements:
#Password Strength Indicator:
#
#Implement a visual indicator of password strength based on the generated password's complexity.
#History:
#
#Include a section to display the history of generated passwords.
#Settings Persistence:
#
#Allow users to save their preferred settings, so they don't need to set them every time.
#Unit Testing:
#
#Write unit tests for the password generation logic to ensure its correctness.

# Importing modules
import random
import string
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QSlider, QLabel, QMessageBox, QCheckBox
from PyQt5.QtGui import QTextCharFormat, QColor, QPalette
from PyQt5.QtCore import Qt

default_password_length = 15

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Enter password length")
        self.layout.addWidget(self.label)

        self.length_slider = QSlider(Qt.Horizontal)
        self.length_slider.setMinimum(5)
        self.length_slider.setMaximum(128)
        self.length_slider.valueChanged.connect(self.updateSliderValue)
        self.length_slider.valueChanged.connect(self.generate)  # Connect the valueChanged signal to the generate slot
        self.layout.addWidget(self.length_slider)

        self.slider_value_label = QLabel()
        self.layout.addWidget(self.slider_value_label)

        self.uppercase_checkbox = QCheckBox("Include Uppercase Letters")
        self.uppercase_checkbox.setChecked(True)
        self.uppercase_checkbox.stateChanged.connect(self.generate)  # Connect the stateChanged signal to the generate slot
        self.layout.addWidget(self.uppercase_checkbox)

        self.lowercase_checkbox = QCheckBox("Include Lowercase Letters")
        self.lowercase_checkbox.setChecked(True)
        self.lowercase_checkbox.stateChanged.connect(self.generate)  # Connect the stateChanged signal to the generate slot
        self.layout.addWidget(self.lowercase_checkbox)

        self.numbers_checkbox = QCheckBox("Include Numbers")
        self.numbers_checkbox.setChecked(True)
        self.numbers_checkbox.stateChanged.connect(self.generate)  # Connect the stateChanged signal to the generate slot
        self.layout.addWidget(self.numbers_checkbox)

        self.symbols_checkbox = QCheckBox("Include Symbols")
        self.symbols_checkbox.stateChanged.connect(self.generate)  # Connect the stateChanged signal to the generate slot
        self.layout.addWidget(self.symbols_checkbox)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate)
        self.layout.addWidget(self.generate_button)

        self.password_label = QTextEdit()
        self.password_label.setReadOnly(True)
        self.password_label.setPlaceholderText("Your generated password will appear here")
        self.password_label.setStyleSheet("font-size: 20px;")
        self.password_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.password_label)

        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy)
        self.layout.addWidget(self.copy_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear)
        self.layout.addWidget(self.clear_button)

        self.length_slider.setValue(default_password_length) # Set the initial value of the length_slider
        self.updateSliderValue() # Update the length_slider value label
        self.generate()  # Generate an initial password

    def updateSliderValue(self):
        value = self.length_slider.value()
        self.slider_value_label.setText(f"Slider Value: {value}")

    def generate(self):
        password_length = self.length_slider.value()

        # Create a string of the selected character types
        characters = ""
        if self.uppercase_checkbox.isChecked():
            characters += string.ascii_uppercase
        if self.lowercase_checkbox.isChecked():
            characters += string.ascii_lowercase
        if self.numbers_checkbox.isChecked():
            characters += string.digits
        if self.symbols_checkbox.isChecked():
            characters += "@#$%^&*" # Not using string.punctuation because it contains some characters that could cause issues and no puctuation cause its treated like a end of sentence (goes to next line)

        # If no character types are selected, show an error message
        if not characters:
            QMessageBox.warning(self, "Warning", "Please select at least one type of characters")
            return

        # Generate the password
        password = [random.choice(characters) for _ in range(password_length)]
        
        # Clear the QTextEdit
        self.password_label.clear()

        # Create QTextCharFormat objects for each type of character
        letter_format = QTextCharFormat()
        letter_format.setForeground(QColor("white"))
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#6f9df1"))
        symbol_format = QTextCharFormat()
        symbol_format.setForeground(QColor("#e3826f"))

        # Insert the password characters into the QTextEdit with the appropriate formatting
        cursor = self.password_label.textCursor()
        for char in password:
            if char in string.ascii_letters:
                cursor.insertText(char, letter_format)
            elif char in string.digits:
                cursor.insertText(char, number_format)
            else:
                cursor.insertText(char, symbol_format)

    def copy(self):
        password = self.password_label.toPlainText()
        pyperclip.copy(password)

    def clear(self):
        self.password_label.clear()
        self.length_slider.setValue(default_password_length)

app = QApplication([])
app.setStyle("Fusion")
# Create a palette
palette = QPalette()
palette.setColor(QPalette.Window, QColor(24, 28, 36)) # Darker background color
palette.setColor(QPalette.WindowText, QColor(255,255,255)) # Text color
palette.setColor(QPalette.Base, QColor(48,52,60)) # Lighter background color
palette.setColor(QPalette.AlternateBase, QColor(53,57,65)) # Alternate background color (I dont know what this is used for)
palette.setColor(QPalette.Button, QColor(48,52,60)) # Button background color
palette.setColor(QPalette.ButtonText, QColor(255,255,255)) # Button text color

# Set the palette for the application
app.setPalette(palette)



window = PasswordGenerator()
window.show()
app.exec_()