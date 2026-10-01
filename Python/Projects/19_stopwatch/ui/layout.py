"""
Project 19: PyQt5 Digital Stopwatch Program
Notes: 46 and 47 for PyQt5
Description: Create a digital stopwatch program utilizing the PyQt5 GUI
"""

# Third-party or local library imports
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

def create_layout(parent, title, time, start, stop, reset):
    # Create vertical layout manager
    vbox = QVBoxLayout()

    # Space between window edge and contents
    vbox.setContentsMargins(20, 12, 20, 12)
    # Space between title, time, and button row
    vbox.setSpacing(2)

    # Label alignment
    title.setAlignment(Qt.AlignCenter)
    time.setAlignment(Qt.AlignCenter)
    # Add label widgets to layout manager
    vbox.addWidget(title)
    vbox.addWidget(time)

    # Create horizontal layout manager
    hbox = QHBoxLayout()
    # set button spacing
    hbox.setSpacing(8)
    # Horizontal layout for buttons
    hbox.addWidget(start)
    hbox.addWidget(stop)
    hbox.addWidget(reset)
    # Add the button layoput to the main layout
    vbox.addLayout(hbox)

    # send the main layout to the parent (self)
    parent.setLayout(vbox)

    return vbox