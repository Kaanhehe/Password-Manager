import pytest
import string
from PyQt5.QtWidgets import QApplication
from main import PasswordGenerator

@pytest.fixture
def app(qapp, request):
    return PasswordGenerator()

def test_password_length(app):
    # Set the length of the password to 10
    app.length_slider.setValue(10)
    # To make sure at least one checkbox is checked so that the password can be generated and not is empty
    app.uppercase_checkbox.setChecked(True)
    app.lowercase_checkbox.setChecked(False)
    app.numbers_checkbox.setChecked(False)
    app.symbols_checkbox.setChecked(False)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the length of the password is 10
    assert len(password) == 10

def test_password_uppercase(app):
    # Enable uppercase letters only
    app.uppercase_checkbox.setChecked(True)
    app.lowercase_checkbox.setChecked(False)
    app.numbers_checkbox.setChecked(False)
    app.symbols_checkbox.setChecked(False)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains only uppercase letters
    assert password.isupper()

def test_password_lowercase(app):
    # Enable lowercase letters only
    app.uppercase_checkbox.setChecked(False)
    app.lowercase_checkbox.setChecked(True)
    app.numbers_checkbox.setChecked(False)
    app.symbols_checkbox.setChecked(False)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains only lowercase letters
    assert password.islower()

def test_password_numbers(app):
    # Enable numbers only
    app.uppercase_checkbox.setChecked(False)
    app.lowercase_checkbox.setChecked(False)
    app.numbers_checkbox.setChecked(True)
    app.symbols_checkbox.setChecked(False)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains only numbers
    assert password.isdigit()

def test_password_symbols(app):
    # Enable symbols only
    app.uppercase_checkbox.setChecked(False)
    app.lowercase_checkbox.setChecked(False)
    app.numbers_checkbox.setChecked(False)
    app.symbols_checkbox.setChecked(True)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains any symbol from the string.punctuation set
    assert any(char in password for char in string.punctuation)

def test_password_uppercase_lowercase(app):
    # Enable uppercase and lowercase letters only
    app.uppercase_checkbox.setChecked(True)
    app.lowercase_checkbox.setChecked(True)
    app.numbers_checkbox.setChecked(False)
    app.symbols_checkbox.setChecked(False)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains only uppercase and lowercase letters
    assert password.isalpha()

def test_password_uppercase_numbers(app):
    # Enable uppercase letters and numbers only
    app.uppercase_checkbox.setChecked(True)
    app.lowercase_checkbox.setChecked(False)
    app.numbers_checkbox.setChecked(True)
    app.symbols_checkbox.setChecked(False)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains only uppercase letters and numbers
    assert password.isalnum() and password.isupper()

def test_password_uppercase_symbols(app):
    # Enable uppercase letters and symbols only
    app.uppercase_checkbox.setChecked(True)
    app.lowercase_checkbox.setChecked(False)
    app.numbers_checkbox.setChecked(False)
    app.symbols_checkbox.setChecked(True)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains uppercase letters and symbols
    assert password.isupper() and any(char in password for char in string.punctuation)

def test_password_lowercase_numbers(app):
    # Enable lowercase letters and numbers only
    app.uppercase_checkbox.setChecked(False)
    app.lowercase_checkbox.setChecked(True)
    app.numbers_checkbox.setChecked(True)
    app.symbols_checkbox.setChecked(False)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains only lowercase letters and numbers
    assert password.isalnum() and password.islower()

def test_password_lowercase_symbols(app):
    # Enable lowercase letters and symbols only
    app.uppercase_checkbox.setChecked(False)
    app.lowercase_checkbox.setChecked(True)
    app.numbers_checkbox.setChecked(False)
    app.symbols_checkbox.setChecked(True)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains lowercase letters and symbols
    assert password.islower() and any(char in password for char in string.punctuation)

def test_password_numbers_symbols(app):
    # Enable numbers and symbols only
    app.uppercase_checkbox.setChecked(False)
    app.lowercase_checkbox.setChecked(False)
    app.numbers_checkbox.setChecked(True)
    app.symbols_checkbox.setChecked(True)
    # Generate the password
    app.generate()
    # Get the generated password
    password = app.password_label.toPlainText()
    # Check if the password contains at least one digit and at least one symbol
    assert any(char.isdigit() for char in password) and any(char in password for char in string.punctuation)
