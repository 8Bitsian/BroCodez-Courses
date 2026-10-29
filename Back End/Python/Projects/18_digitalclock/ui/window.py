"""
Project 18: PyQt5 Digital Clock Program
Notes: 46 and 47 for PyQt5
Description: Create a digital clock program utilizing the PyQt5 GUI
"""

# Third-party or local library imports
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer, QTime

from ui.label import create_title, create_time
from ui.layout import create_layout

# Customize window and display to end user
class MainWindow(QMainWindow):
    # Constructor/Initialization Method
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Digital Alarm Clock")
        self.setFixedSize(500, 200)

        # Sourced from: https://feathericons.com/?query=clock
        self.setWindowIcon(QIcon(r"Python\Projects\18_digitalclock\images\clock.svg"))

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # labels = create_clock(central_widget)
        self.title = create_title(central_widget)
        self.time = create_time(central_widget)

        create_layout(central_widget, self.title, self.time)

        # timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time.setText(current_time)