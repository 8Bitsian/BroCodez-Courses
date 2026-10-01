"""
Project 18: PyQt5 Digital Clock Program
Notes: 46 and 47 for PyQt5
Description: Create a digital clock program utilizing the PyQt5 GUI
"""

# Third-party or local library imports
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QTimer, QTime

def create_label(parent, object_name, text=""):
    label = QLabel(text, parent)
    label.setObjectName(object_name)
    return label

def create_title(parent):
    return create_label(parent, "title",
                        "Digital Alarm Clock")

def create_time(parent):
    return create_label(parent, "time")