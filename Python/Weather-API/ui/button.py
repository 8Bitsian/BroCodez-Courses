# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Third-party imports
from PyQt5.QtWidgets import QPushButton, QRadioButton, QButtonGroup

def create_button(parent, object_name, module, text=""):
    """Create the button object w/specified parameters."""
    # Create button object
    button = QPushButton(text, parent)
    # Set the name for reference in style sheet
    button.setObjectName(object_name)
    # Connect the button object to a module
    button.clicked.connect(module)

    return button

def create_submit(parent, on_submit_click):
    """Create the submit button to enter the city name."""
    return create_button(parent, "submit", on_submit_click, "Submit")

def create_radio(parent, object_name, module, text=""):
    """Create the radio button object w/specified parametrs."""\
    # Create the radio button object
    radio = QRadioButton(text, parent)
    # Set the name for reference in style sheet
    radio.setObjectName(object_name)
    # Connect the button object to a module
    radio.clicked.connect(module)

    return radio

def create_temp_preference(parent, on_unit_changed):
    """
    Create the temperature-unit radio buttons.

    The button IDs mathc OpenWeather's API unit values:
    metric = Celsius
    imperial = Fahrenheit
    """
    # Create radio button objects
    celsius = create_radio(parent, "c-temp", on_unit_changed, "Celsius")
    fahrenheit = create_radio(parent, "f-temp", on_unit_changed, "Fahrenheit")
    
    # Put the radio buttons into one group
    temp_group = QButtonGroup(parent)
    temp_group.addButton(celsius, 0)
    temp_group.addButton(fahrenheit, 1)

    # Connect the group
    temp_group.idClicked.connect(on_unit_changed)

    # Celsius is selected by default
    celsius.setChecked(True)

    return (fahrenheit, celsius)