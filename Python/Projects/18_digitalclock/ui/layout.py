"""
Project 18: PyQt5 Digital Clock Program
Notes: 46 and 47 for PyQt5
Description: Create a digital clock program utilizing the PyQt5 GUI
"""

# Third-party or local library imports
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt

def create_layout(parent, title, time):
    vbox = QVBoxLayout()

    title.setAlignment(Qt.AlignCenter)
    vbox.addWidget(title)

    time.setAlignment(Qt.AlignCenter)
    vbox.addWidget(time)

    parent.setLayout(vbox)

    return vbox