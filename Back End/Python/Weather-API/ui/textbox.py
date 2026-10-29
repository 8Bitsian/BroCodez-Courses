# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Third party imports
from PyQt5.QtWidgets import QLineEdit

def create_textbox(parent, object_name, text="", password=False):
    """Create a lineedit (textbox) object w/specified parameters for end users to enter thier city name."""
    # Create textbox object
    textbox = QLineEdit(parent)
    # Set the name for reference in style sheet
    textbox.setObjectName(object_name)
    # Set the placeholder text for the textbox
    textbox.setPlaceholderText(text)

    if password:
        textbox.setEchoMode(QLineEdit.Password)

    return textbox

def create_city_input(parent):
    """Create the city name input text box to enter the city name."""
    return create_textbox(parent, "cityInput", "Enter City Name")

def create_api_key_input(parent):
    """Create the api key textbox to enter openweatherapp.org API key."""
    return create_textbox(parent, "apiKeyInput", "Enter OpenWeather API Key", password=True)