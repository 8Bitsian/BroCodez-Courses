# pyQt5 GUI Line Edit (Text Boxes)

# Third-party or local library imports
# Widgets are the building blocks of any PyQt5 application.
# They begin with `Q` to help distinguish them from other libraries widgets.
# The `QLineEdit` module is designed for creating text boxes
from PyQt5.QtWidgets import QLineEdit
# The `QFont` module is designed to work with text and change fonts
from PyQt5.QtGui import QFont

def create_textbox(parent):
    # To create a textbox, be sure to prefix w/the `self` object when in the initial construtor method. When defining a standalone function, just call the `QLineEdit()` method and initialize the button object w/a string and the self object.
    textbox = QLineEdit(parent)

    # You are able to stylize a textbox as you would any other widget.
    textbox.setFont(QFont("JetBrains Mono", 15, 600))
    textbox.setStyleSheet("color: #8C52FF;"
                          "background-color: #FFFFF0;")

    # To can use the `setPlaceholderText() method w/a string paramter to have the textbox initally show a string prior to typing`
    textbox.setPlaceholderText("Type here and submit...")

    # To have the button do something when clicked use the `clicked.connect()` method and pass in a function for what you would like to happen as the parameter.
    # button.clicked.connect(on_button_click)

    return textbox