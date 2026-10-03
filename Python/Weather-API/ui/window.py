"""
Final Project: Weather API Application
Description: A weather app that gets API data to show real-time weather.
"""

# Third-party imports
from PyQt5.QtWidgets import QMainWindow, QWidget, QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# Local library imports
# from buttons import (create_button,
#                      create_submission, create_radio_button)
# from checkboxes import create_checkbox
# from textboxes import create_textbox
# from labels import create_title, color_title
# from pictures import create_picture
# from layouts import create_layout

class MainWindow(QMainWindow):
    # Initialization Method
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather API App")
        self.setGeometry(700, 300, 500, 500)
        # Sourced from: https://feathericons.com/?query=weather
        self.setWindowIcon(QIcon(r"Python\Weather-API\images\cloud-drizzle.svg"))
