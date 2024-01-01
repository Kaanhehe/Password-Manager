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
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

# Setting up the window
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Password Generator")
root.config(bg="lightblue")

# Defining variables
pass_str = StringVar()
pass_len = IntVar()
pass_len.set(0)
pass_str.set("")

# Defining functions
def generate():
    if pass_len.get() == 0:
        messagebox.showerror("Error", "Please enter a password length")
    else:
        password = ""
        for x in range(pass_len.get()):
            password = password + random.choice(string.ascii_letters + string.digits + string.punctuation)
        pass_str.set(password)

def copy():
    pyperclip.copy(pass_str.get())
    messagebox.showinfo("Success", "Password copied to clipboard")

def clear():
    pass_str.set("")
    pass_len.set(0)

# Creating the GUI
Label(root, text="Password Generator", font="arial 15 bold").pack()
Label(root, text="Enter password length", font="arial 10 bold").pack(pady=10)
Entry(root, textvariable=pass_len, width=20).pack(pady=10)
Button(root, text="Generate Password", command=generate).pack(pady=10)
Entry(root, textvariable=pass_str, width=20).pack(pady=10)
Button(root, text="Copy to Clipboard", command=copy).pack(pady=10)
Button(root, text="Clear", command=clear).pack(pady=10)

# Running the mainloop
root.mainloop()