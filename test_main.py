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