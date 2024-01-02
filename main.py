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
import secrets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QSlider, QLabel, QMessageBox, QCheckBox
from PyQt5.QtGui import QTextCharFormat, QColor, QPalette
from PyQt5.QtCore import Qt

default_password_length = 15
colors = {
    "symbols" : "#c95740",
    "numbers" : "#6f9df1",
    "letters" : "white"
}

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle('Password Generator')
        
        # Set the window size
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Password label
        self.password_label = QTextEdit()
        self.password_label.setReadOnly(True) # Make the password label read-only
        self.password_label.setPlaceholderText("Das Passwort wird hier angezeigt")
        self.password_label.setStyleSheet("font-size: 20px;")
        self.layout.addWidget(self.password_label) # Add the password label to the layout

        self.generate_password_options()
        self.generate_buttons()

        # Set the initial state of the widgets
        self.length_slider.setValue(default_password_length) # Set the initial value of the length_slider
        self.updateSliderValue() # Update the length_slider value label
        self.generate()  # Generate an initial password

    def generate_password_options(self):
        #! -- Widgets for the password generation options -- !#
            
        # - Passwortlänge - #
        # Passwortlänge label
        self.label = QLabel("Passwortlänge")
        self.layout.addWidget(self.label)

        # Passwortlänge slider
        self.length_slider = QSlider(Qt.Horizontal)
        self.length_slider.setMinimum(5)
        self.length_slider.setMaximum(128)
        self.length_slider.valueChanged.connect(self.updateSliderValue) # Update the length_slider value label when the slider is moved
        self.length_slider.valueChanged.connect(self.generate) # Generate a new password when the slider is moved
        self.layout.addWidget(self.length_slider)

        # Passwortlänge slider value label
        self.slider_value_label = QLabel()
        self.layout.addWidget(self.slider_value_label)

        # - Zeichenarten Checkboxes - #
        # Zeichenarten label
        self.charlabel = QLabel("Zeichenarten")
        self.layout.addWidget(self.charlabel)

        # Uppercase checkbox
        self.uppercase_checkbox = QCheckBox("A-Z")
        self.uppercase_checkbox.setChecked(True)
        self.uppercase_checkbox.stateChanged.connect(self.generate) # Generate a new password when the checkbox is checked/unchecked
        self.layout.addWidget(self.uppercase_checkbox)

        # Lowercase checkbox
        self.lowercase_checkbox = QCheckBox("a-z")
        self.lowercase_checkbox.setChecked(True)
        self.lowercase_checkbox.stateChanged.connect(self.generate) # Generate a new password when the checkbox is checked/unchecked 
        self.layout.addWidget(self.lowercase_checkbox)

        # Numbers checkbox
        self.numbers_checkbox = QCheckBox("0-9")
        self.numbers_checkbox.setChecked(True)
        self.numbers_checkbox.stateChanged.connect(self.generate) # Generate a new password when the checkbox is checked/unchecked
        self.layout.addWidget(self.numbers_checkbox)

        # Symbols checkbox
        self.symbols_checkbox = QCheckBox("@#$%^&*")
        self.symbols_checkbox.stateChanged.connect(self.generate) # Generate a new password when the checkbox is checked/unchecked
        self.layout.addWidget(self.symbols_checkbox)
        
    def generate_buttons(self):
        #! -- Buttons -- !#
        # regenerate button
        self.generate_button = QPushButton("Passwort neu generieren")
        self.generate_button.clicked.connect(self.generate) # Generate a new password when the button is clicked
        self.layout.addWidget(self.generate_button)

        # copy button
        self.copy_button = QPushButton("Passwort kopieren")
        self.copy_button.clicked.connect(self.copy)
        self.layout.addWidget(self.copy_button)

        # clear button
        self.clear_button = QPushButton("Passwort löschen")
        self.clear_button.clicked.connect(self.clear)
        self.layout.addWidget(self.clear_button)

    def updateSliderValue(self):
        value = self.length_slider.value()
        self.slider_value_label.setText(f"Passwortlänge: {value}")

    def getcharacters(self):
        # Get the selected character types
        character_groups = []
        if self.uppercase_checkbox.isChecked():
            character_groups.append(string.ascii_uppercase)
        if self.lowercase_checkbox.isChecked():
            character_groups.append(string.ascii_lowercase)
        if self.numbers_checkbox.isChecked():
            character_groups.append(string.digits)
        if self.symbols_checkbox.isChecked():
            character_groups.append("@#$%^&*")
        
        return character_groups
    
    def generatepassword(self, password_length, character_groups):
        # Generate the password
        password = []
        # First, add one character from each group
        for group in character_groups:
            password.append(secrets.choice(group))
        # Then, fill the rest of the password with characters from all groups
        all_characters = "".join(character_groups)
        password += (secrets.choice(all_characters) for _ in range(password_length - len(character_groups)))

        # Shuffle the password to ensure the characters from different groups are not clumped together
        random.shuffle(password)

        # Convert the password list to a string
        password = "".join(password)

        return password

    def generate(self): # The password generation is a little complicated to ensure there is at least one character from each selected group
        password_length = self.length_slider.value()

        character_groups = self.getcharacters()

        # Ensure at least one character group is selected
        if not character_groups:
            QMessageBox.warning(self, "Warning", "Please select at least one type of characters")
            return

        # Ensure the password length is at least the number of character groups
        if password_length < len(character_groups):
            QMessageBox.warning(self, "Warning", "Password length must be at least the number of selected character types")
            return

        password = self.generatepassword(password_length, character_groups)

        # Clear the password label
        self.password_label.clear()

        # Set the password label's text colors
        letter_format = QTextCharFormat()
        letter_format.setForeground(QColor(colors["letters"]))
        number_format = QTextCharFormat()
        number_format.setForeground(QColor(colors["numbers"]))
        symbol_format = QTextCharFormat()
        symbol_format.setForeground(QColor(colors["symbols"]))

        # Insert the password characters into the password label with the correct colors
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

# Create the application
app = QApplication([])
app.setStyle("Fusion")

# Create the palette for the application
palette = QPalette()
palette.setColor(QPalette.Window, QColor(24, 28, 36)) # Darker background color
palette.setColor(QPalette.WindowText, QColor(255,255,255)) # Text color
palette.setColor(QPalette.Base, QColor(48,52,60)) # Lighter background color
palette.setColor(QPalette.AlternateBase, QColor(53,57,65)) # Alternate background color (I dont know what this is used for)
palette.setColor(QPalette.Button, QColor(48,52,60)) # Button background color
palette.setColor(QPalette.ButtonText, QColor(255,255,255)) # Button text color

# Set the palette for the application
app.setPalette(palette)

# Create the application window
window = PasswordGenerator()
window.show()
app.exec_()