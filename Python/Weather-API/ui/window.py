# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Standard-library imports
import sys, os
from pathlib import Path

# Third-party imports
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt

# Local library imports
from data.apidata import load_weather_data

from ui.button import (create_submit,
                       create_temp_preference)

from ui.image import (load_icon,
                      create_picture,
                      update_picture)

from ui.label import (create_title,
                      create_temperature,
                      create_caption)

from ui.layout import create_layout

from ui.textbox import (create_api_key_input,
                        create_city_input)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up basic window description
        self.setWindowTitle("Weather API App")
        self.setMinimumSize(400, 600)
        # Image sourced from https://feathericons.com/
        self.setWindowIcon(load_icon("cloud-drizzle.svg"))

        # Create temperature unit data variables for radio buttons
        self.units = "metric"
        self.last_request = None
        self.last_weather_data = None

        # Create a UI with a generic central widget and a layout manager
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create title object
        self.title = create_title(central_widget)

        # Create api and city textboxes and submit buttons
        self.api_key = create_api_key_input(central_widget)
        # create separate submit button for api key
        self.city_name = create_city_input(central_widget)
        self.submit = create_submit(central_widget, self.on_submit_click)

        # Create temperature label and measurement buttons
        self.temperature = create_temperature(central_widget)
        self.fahrenheit, self.celsius = create_temp_preference(central_widget,
                                                               self.on_unit_changed)

        # Create weather icon and caption objects
        self.picture = create_picture(central_widget)
        self.caption = create_caption(central_widget)

        # Apply the layout manager to the entire UI
        widgets = {
            "title": self.title,
            "api_key": self.api_key,
            "city_name": self.city_name,
            "submit": self.submit,
            "temperature": self.temperature,
            "fahrenheit": self.fahrenheit,
            "celsius": self.celsius,
            "picture": self.picture,
            "caption": self.caption
        }

        create_layout(central_widget, widgets)

    def on_submit_click(self):
        print("Submit Clicked!")

        api_key = self.api_key.text().strip()
        if not api_key:
            self.caption.setText("Please enter your API key.")
            return

        city_name = self.city_name.text().strip()
        if not city_name:
            self.caption.setText("Please enter a city.")
            return

        print(f"You submitted: {city_name}")

        request_key = city_name.casefold()
        if request_key == self.last_request:
            self.caption.setText("Data is already being displayed")
            return

        self.submit.setEnabled(False)
        self.caption.setText("Loading weather...")

        try:
            data = load_weather_data(city_name, api_key, "metric")
            self.last_weather_data = data
            self.last_request = request_key

            self.display_weather(data)

        except ValueError as error:
            self.caption.setText(str(error))

        finally:
            self.submit.setEnabled(True)

    def on_unit_changed(self, button_id):
        self.units = "imperial" if button_id == 1 else "metric"
        if self.last_weather_data is None:
            self.caption.setText("Submit a city to load the weather.")
            return

        self.display_weather(self.last_weather_data)

    def display_weather(self, data):
        main_data = data.get("main", {})
        weather_data = data.get("weather", [{}])[0]

        temperature = main_data.get("temp")
        description = weather_data.get("description", "Unknown").capitalize()
        condition = weather_data.get("main", "")

        if temperature is None:
            self.caption.setText("The weather response was incomplete.")
            return

        # If saved response was originally loaded in Celsius, convert it to Fahrenheit
        if self.units == "imperial":
            temperature = (temperature * 9 / 5) + 32
            unit_symbol = "°F"
        else:
            unit_symbol = "°C"

        self.temperature.setText(f"{temperature:.1f}{unit_symbol}")

        city_name = data.get("name", self.city_name.text().strip())
        self.caption.setText(f"{city_name}: {description}")

        icon_filename = {
            "Clear": "sun.svg",
            "Clouds": "cloud.svg",
            "Rain": "cloud-rain.svg",
            "Thunderstorm": "cloud-lightning.svg",
            "Snow": "cloud-snow.svg",
        }.get(condition, "cloud-drizzle.svg")

        update_picture(self.picture, icon_filename)