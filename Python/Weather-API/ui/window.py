# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Standard-library imports
import sys, os
from pathlib import Path

# Third-party imports
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt

# Local library imports
from ui.image import (load_icon,
                      create_picture,
                      update_picture)

from ui.button import (create_submit,
                       create_temp_preference)

from ui.textbox import create_city_input

from ui.label import (create_title,
                      create_temperature,
                      create_caption)

from ui.layout import create_layout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up basic window description
        self.setWindowTitle("Weather API App")
        self.setGeometry(700, 300, 500, 500)
        # Image sourced from https://feathericons.com/
        self.setWindowIcon(load_icon("cloud-drizzle.svg"))

        # Create a UI with a generic central widget and a layout manager
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create title object
        self.title = create_title(central_widget)

        # Create city textbox and submit button
        self.textbox = create_city_input(central_widget)
        self.submit = create_submit(central_widget,
                                    self.on_submit_click)

        # Create temperature label and measurement buttons
        self.temperature = create_temperature(central_widget)
        self.fahrenheit, self.celsius = create_temp_preference(central_widget,
                                                               self.state_change)

        # Create weather icon and caption objects
        self.picture = create_picture(central_widget)
        self.caption = create_caption(central_widget)

        # Apply the layout manager to the entire UI
        widgets = [self.title,
                  self.textbox,
                  self.submit,
                  self.temperature,
                  self.fahrenheit,
                  self.celsius,
                  self.picture,
                  self.caption]

        create_layout(central_widget, widgets)

    def on_submit_click(self):
        print("Submit Clicked!")

        city = self.textbox.text().strip()

        if not city:
            self.caption.setText("Please enter a city.")
            return

        print(f"You submitted: {city}")

        update_picture(self.picture, "sun.svg")
        self.caption.setText("Sunny")

        degree = 25
        if self.fahrenheit.isChecked():
            temperature = {degree * 9 / 5} + 32
            self.temperature.setText(f"{temperature:.1f}°F")
        else:
            self.temperature.setText(f"{degree:.1f}°C")

    def state_change(self, button_id):
        if button_id == 0:  
            print("Fahrenheit Selected!")
        elif button_id == 1:
            print("Celsius Selected!")