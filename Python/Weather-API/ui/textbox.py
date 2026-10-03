# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Third party imports
from PyQt5.QtWidgets import QLineEdit

def create_textbox(parent, object_name, text=""):
    """Create a lineedit (textbox) object w/specified parameters for end users to enter thier city name."""
    # Create textbox object
    textbox = QLineEdit(parent)
    # Set the name for reference in style sheet
    textbox.setObjectName(object_name)
    # Set the placeholder text for the textbox
    textbox.setPlaceholderText(text)

    return textbox

def create_city_input(parent):
    """Create the submit button to enter the city name."""
    return create_textbox(parent, "textbox",
                         "Enter City Name: ")