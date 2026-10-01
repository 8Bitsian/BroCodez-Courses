"""
Project 19: PyQt5 Digital Stopwatch Program
Notes: 46 and 47 for PyQt5
Description: Create a digital stopwatch program utilizing the PyQt5 GUI
"""

# Third-party or local library imports
from PyQt5.QtWidgets import QPushButton

def create_button(parent, object_name, text=""):
    button = QPushButton(text, parent)
    button.setObjectName(object_name)
    return button

def create_start(parent, on_button_click):
    # Create a button
    start_button = create_button(parent, "start", "Start Stopwatch")
    # Connect the button to a function when clicked
    start_button.clicked.connect(on_button_click)
    return start_button

def create_stop(parent, on_button_click):
    stop_button = create_button(parent, "stop", "Stop Stopwatch")
    stop_button.clicked.connect(on_button_click)
    return stop_button

def create_reset(parent, on_button_click):
    reset_button = create_button(parent, "reset", "Reset Stopwatch")
    reset_button.clicked.connect(on_button_click)
    return reset_button