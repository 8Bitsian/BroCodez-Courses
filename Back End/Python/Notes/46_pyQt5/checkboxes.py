# pyQt5 GUI Buttons
# standard Library Imports
import sys

# Third-party or local library imports
# Widgets are the building blocks of any PyQt5 application.
# They begin with `Q` to help distinguish them from other libraries widgets.
# The `QPushButton` module is designed for creating buttons
from PyQt5.QtWidgets import QCheckBox
# The `Qt` module is used for alignments
from PyQt5.QtCore import Qt
# The `QFont` module is designed to work with text and change fonts
from PyQt5.QtGui import QFont

def create_checkbox(parent, checkbox_changed):
    # To create a checkbox, be sure to prefix w/the self object when in the initial construtor method. When defining a standalone function, just call the `QCheckBox()` method and initialize the button object w/a string and the self object.
    checkbox = QCheckBox("Do you like purple?", parent)

    # You are able to stylize a checkbox as you would any other widget.
    checkbox.setFont(QFont("JetBrains Mono", 15, 300))
    checkbox.setStyleSheet("color: #FFFFF0;"
                           "background-color: #8C52FF;")

    # To set the inital state of the checkbox, use the `setChecked()` method and pass the either the boolean parameter `False` for unchecked, or `True` for checked.
    checkbox.setChecked(False)

    # To have the checkbox do something when clicked use the `clicked.stateChanged()` method and pass in a function for what you would like to happen as the parameter.
    checkbox.stateChanged.connect(checkbox_changed)

    return checkbox