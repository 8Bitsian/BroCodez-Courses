"""
Project 19: PyQt5 Digital Stopwatch Program
Notes: 46 and 47 for PyQt5
Description: Create a digital stopwatch program utilizing the PyQt5 GUI
"""

# Third-party or local library imports
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QIcon

from ui.label import create_title, create_time
from ui.button import create_start, create_stop, create_reset
from ui.layout import create_layout

# Customize window and display to end user
class MainWindow(QMainWindow):
    # Constructor/Initialization Method
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Digital Stopwatch")
        self.setFixedSize(500, 200)

        # Sourced from: https://feathericons.com/?query=time
        self.setWindowIcon(QIcon(r"Python\Projects\19_stopwatch\images\clock.svg"))

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create label widgets
        self.title = create_title(central_widget)
        self.time_label = create_time(central_widget)

        # Create button widgets
        self.start_button = create_start(central_widget, self.on_button_click)
        self.stop_button = create_stop(central_widget, self.on_button_click)
        self.reset_button = create_reset(central_widget, self.on_button_click)

        # Apply layout managers
        create_layout(central_widget,
                      self.title,
                      self.time_label,
                      self.start_button,
                      self.stop_button,
                      self.reset_button)

        # Time object used to display the time
        self.time = QTime(0, 0, 0, 0)

        # Timer object used to update the time via a function call
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.update_time()

    def on_button_click(self):
        button = self.sender()

        if button.objectName() == "start":
            self.start()
        elif button.objectName() == "stop":
            self.stop()
        elif button.objectName() == "reset":
            self.reset()

    def start(self):
        print("Stopwatch Started")
        self.timer.start(10)

    def stop(self):
        print("Stopwatch Stopped")
        self.timer.stop()

    def reset(self):
        print("Stopwatch Reset")
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
        # current_time = QTime.currentTime().toString("hh:mm:ss AP")
        # self.time_label.setText(current_time)