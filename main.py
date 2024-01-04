#Clean and Responsive Design:
#
#Create a clean and user-friendly design for the GUI.
#Ensure that the interface is responsive and works well on different screen sizes.
#Error Handling:
#
#Implement error handling to manage scenarios like invalid input or password generation failure.
#Provide informative messages to guide the user in case of errors.
# Importing modules
import random
import string
import pyperclip
import secrets
from zxcvbn import zxcvbn
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QSlider, QLabel, QMessageBox, QCheckBox, QProgressBar
from PyQt5.QtGui import QTextCharFormat, QColor, QPalette
from PyQt5.QtCore import Qt, QSettings, QRect, QPoint, QSize

default_password_length = 15
colors = {
    "symbols" : "#c95740",
    "numbers" : "#6f9df1",
    "letters" : "white"
}

class PasswordGenerator(QWidget):
    """
    !!!!This Documentation was written by Github Copilot not by me!!!!

    A class that represents a password generator widget.

    Attributes:
        settings (QSettings): A QSettings object for storing and retrieving settings.
        password_label (QTextEdit): A QTextEdit widget for displaying the generated password.
        password_strength_bar (QProgressBar): A QProgressBar widget for displaying the password strength.
        uppercase_checkbox (QCheckBox): A QCheckBox widget for selecting uppercase characters.
        lowercase_checkbox (QCheckBox): A QCheckBox widget for selecting lowercase characters.
        numbers_checkbox (QCheckBox): A QCheckBox widget for selecting numeric characters.
        symbols_checkbox (QCheckBox): A QCheckBox widget for selecting symbol characters.
        length_slider (QSlider): A QSlider widget for selecting the length of the password.
        slider_value_label (QLabel): A QLabel widget for displaying the value of the length slider.
        generate_button (QPushButton): A QPushButton widget for generating a new password.
        copy_button (QPushButton): A QPushButton widget for copying the generated password.
        clear_button (QPushButton): A QPushButton widget for clearing the generated password.

    Methods:
        initUI(): Initializes the user interface of the password generator widget.
        generate_password_options(): Creates the widgets for the password generation options.
        generate_buttons(): Creates the buttons for generating, copying, and clearing the password.
        updateSliderValue(): Updates the value label of the length slider.
        getcharacters(): Retrieves the selected character types.
        generatepassword(password_length, character_groups): Generates a password based on the selected options.
        calculate_password_strength(password): Calculates the strength of the generated password.
        generate(): Generates a new password based on the selected options.
        copy(): Copies the generated password to the clipboard.
        clear(): Clears the generated password.
        closeEvent(event): Handles the close event of the password generator widget.
    """
        
    def __init__(self):
        super().__init__()

        # Create a QSettings object
        self.settings = QSettings("Kaanhehe", "Password Generator")

        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle('Password Generator')
        
        # Set the window size
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setFixedSize(350, 500)

        # Password label
        self.password_label = QTextEdit()
        self.password_label.setReadOnly(True) # Make the password label read-only
        self.password_label.setPlaceholderText("Das Passwort wird hier angezeigt")
        self.password_label.setStyleSheet("font-size: 20px;")
        self.password_label.setMaximumWidth(int(self.width() * 0.8))
        self.layout.addWidget(self.password_label) # Add the password label to the layout


        self.generate_password_options()

        self.password_strength_bar = QProgressBar(self)
        self.layout.addWidget(self.password_strength_bar)

        self.generate_buttons()

        # Load the state of the checkboxes and slider from the settings
        self.uppercase_checkbox.setChecked(self.settings.value("uppercase", True, type=bool))
        self.lowercase_checkbox.setChecked(self.settings.value("lowercase", True, type=bool))
        self.numbers_checkbox.setChecked(self.settings.value("numbers", True, type=bool))
        self.symbols_checkbox.setChecked(self.settings.value("symbols", True, type=bool))
        self.length_slider.setValue(self.settings.value("length", default_password_length, type=int))

        # Set the initial state of the widgets
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
        self.uppercase_checkbox.stateChanged.connect(self.generate) # Generate a new password when the checkbox is checked/unchecked
        self.layout.addWidget(self.uppercase_checkbox)

        # Lowercase checkbox
        self.lowercase_checkbox = QCheckBox("a-z")
        self.lowercase_checkbox.stateChanged.connect(self.generate) # Generate a new password when the checkbox is checked/unchecked 
        self.layout.addWidget(self.lowercase_checkbox)

        # Numbers checkbox
        self.numbers_checkbox = QCheckBox("0-9")
        self.numbers_checkbox.stateChanged.connect(self.generate) # Generate a new password when the checkbox is checked/unchecked
        self.layout.addWidget(self.numbers_checkbox)

        # Symbols checkbox
        self.symbols_checkbox = QCheckBox("@#$%^&*")
        self.symbols_checkbox.stateChanged.connect(self.generate) # Generate a new password when the checkbox is checked/unchecked
        self.layout.addWidget(self.symbols_checkbox)
        
    def generate_buttons(self):
        #! -- Buttons -- !#
        # regenerate button
        self.generate_button = QPushButton("Passwort\nneu\ngenerieren", self)
        self.generate_button.setGeometry(QRect(QPoint(295, 11), QSize(50, 85)))
        self.generate_button.clicked.connect(self.generate) # Generate a new password when the button is clicked

        # copy button
        self.copy_button = QPushButton("Passwort\nkopieren", self)
        self.copy_button.setGeometry(QRect(QPoint(295, 105), QSize(50, 85)))
        self.copy_button.clicked.connect(self.copy) # Copy the password to the clipboard when the button is clicked

        # clear button
        self.clear_button = QPushButton("Passwort\nlöschen", self)
        self.clear_button.setGeometry(QRect(QPoint(295, 199), QSize(50, 85)))
        self.clear_button.clicked.connect(self.clear)

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
    
    def calculate_password_strength(self, password):
        results = zxcvbn(password)
        crack_time = results['crack_times_display']['offline_slow_hashing_1e4_per_second']

        # Extract the numeric part from the crack_time
        numeric_part = re.search(r'\d+', crack_time)
        if numeric_part is not None:
            numeric_part = int(numeric_part.group())
        else:
            numeric_part = 0

        if 'centuries' in crack_time:
            score = 10
        elif 'year' in crack_time:
            score = 4 + (numeric_part / 10)  # Adjust score based on the number of years
        elif 'month' in crack_time:
            score = 2 + (numeric_part / 12)  # Adjust score based on the number of months
        elif 'day' in crack_time:
            score = 0.5 + (numeric_part / 30)  # Adjust score based on the number of days
        elif 'hour' in crack_time:
            score = 0 + (numeric_part / 24)  # Adjust score based on the number of hours
        else:
            score = 0

        # Multiply by 10 and round to get a whole number
        score = round(score * 10)
        return min(score, 100)

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

        if not password:
            QMessageBox.warning(self, "Warning", "Failed to generate password")
            return

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

        password_strength = self.calculate_password_strength(password)
        self.password_strength_bar.setValue(password_strength)

    def copy(self):
        password = self.password_label.toPlainText()
        pyperclip.copy(password)

    def clear(self):
        self.password_label.clear()
        self.length_slider.setValue(default_password_length)

    def closeEvent(self, event):
        # Save the state of the checkboxes
        self.settings.setValue("length", self.length_slider.value())
        self.settings.setValue("uppercase", self.uppercase_checkbox.isChecked())
        self.settings.setValue("lowercase", self.lowercase_checkbox.isChecked())
        self.settings.setValue("numbers", self.numbers_checkbox.isChecked())
        self.settings.setValue("symbols", self.symbols_checkbox.isChecked())

        super().closeEvent(event)

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

if __name__ == "__main__":
    window = PasswordGenerator()
    window.show()
    app.exec_()