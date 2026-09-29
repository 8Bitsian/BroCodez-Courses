# pyQt5 GUI Buttons

# Third-party or local library imports
# Widgets are the building blocks of any PyQt5 application.
# They begin with `Q` to help distinguish them from other libraries widgets.
# The `QPushButton` module is designed for creating buttons
# The `QRadioButton` module is designed for creating radio buttons
# The `QButtonGroup` module is designed for groupiing sets of buttons together
from PyQt5.QtWidgets import (QPushButton, QRadioButton, QButtonGroup)
# The `QFont` module is designed to work with text and change fonts
from PyQt5.QtGui import QFont

def create_button(parent, on_button_click):
    # To create a button, be sure to prefix w/the self object when in the initial construtor method. When defining a standalone function, just call the `QPushButton()` method and initialize the button object w/a string and the self object.
    button = QPushButton("Click Me!", parent)
    # You are able to stylize a button as you would any other widget.
    button.setFont(QFont("JetBrains Mono", 25, 600))
    button.setStyleSheet("color: #FFFFF0;"
                         "background-color: #8C52FF;")

    # To have the button do something when clicked use the `clicked.connect()` method and pass in a function for what you would like to happen as the parameter.
    button.clicked.connect(on_button_click)

    return button

def create_radio_button(parent, on_radio_click):
    radios = [
        QRadioButton("I like Transformers!", parent),
        QRadioButton("I like Gundam ZERO!", parent),
        QRadioButton("I like Warthammer 40K!", parent),
        QRadioButton("Comics/Manga", parent),
        QRadioButton("Animated Series", parent)
    ]

    parent.setStyleSheet("QRadioButton{"
                            "font-family: JetBrains Mono;"
                            "font-size: 15px;"
                            "padding: 5px;"
                         "}")

    button_group1 = QButtonGroup(parent)
    for radio in radios[:3]:
        button_group1.addButton(radio)

    button_group2 = QButtonGroup(parent)
    for radio in radios[3:]:
        button_group2.addButton(radio)

    # To have the button do something when clicked use the `clicked.toggled()` method and pass in a function for what you would like to happen as the parameter.
    for radio in radios:
        radio.toggled.connect(on_radio_click)

    return radios