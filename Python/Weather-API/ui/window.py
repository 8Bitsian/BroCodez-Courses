# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Third-party imports
from PyQt5.QtWidgets import QMainWindow, QWidget

# Local library imports
from .image import load_icon
# from buttons import (create_button,
#                      create_submission, create_radio_button)
# from checkboxes import create_checkbox
# from textboxes import create_textbox
# from labels import create_title, color_title
# from layouts import create_layout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather API App")
        self.setGeometry(700, 300, 500, 500)

        # window.py is in Weather-API/ui/
        self.setWindowIcon(load_icon("cloud-drizzle.svg"))