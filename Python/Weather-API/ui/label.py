# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Third party imports
from PyQt5.QtWidgets import QLabel

def create_label(parent, object_name, text=""):
    """Create the label object w/specified parameters."""
    # Create label object
    label = QLabel(text, parent)
    # Set the name for reference in style sheet
    label.setObjectName(object_name)
    return label

def create_title(parent):
    """Create the title label for the program."""
    return create_label(parent, "title",
                        "Weather API App")

def create_temperature(parent):
    """Create the temperature label."""
    return create_label(parent, "temperature",
                        "--")

def create_caption(parent):
    """Create the caption label for the weather icons."""
    return create_label(parent, "caption",
                        "Enter a city to begin.")