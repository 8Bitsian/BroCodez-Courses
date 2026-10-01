"""
Project 19: PyQt5 Digital Stopwatch Program
Notes: 46 and 47 for PyQt5
Description: Create a digital stopwatch program utilizing the PyQt5 GUI
"""

# Third-party or local library imports
from PyQt5.QtWidgets import QLabel

def create_label(parent, object_name, text=""):
    label = QLabel(text, parent)
    label.setObjectName(object_name)
    return label

def create_title(parent):
    return create_label(parent, "title",
                        "Digital Alarm Clock")

def create_time(parent):
    return create_label(parent, "time", "00:00:00.00")