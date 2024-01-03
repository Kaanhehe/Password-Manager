import pytest
from PyQt5.QtWidgets import QApplication
from main import PasswordGenerator

@pytest.fixture
def app(qapp, request):
    return PasswordGenerator()

def test_password_length(app):
    app.length_slider.setValue(10)
    app.generate()
    assert len(app.password_line_edit.text()) == 10

def test_password_uppercase(app):
    app.uppercase_checkbox.setChecked(True)
    app.lowercase_checkbox.setChecked(False)
    app.numbers_checkbox.setChecked(False)
    app.symbols_checkbox.setChecked(False)
    app.generate()
    assert app.password_line_edit.text().isupper()

# Add more tests for lowercase, numbers, and symbols