# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Third-party imports
from PyQt5.QtWidgets import QPushButton, QRadioButton, QButtonGroup

def create_button(parent, module, object_name, text=""):
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
    return create_button(parent,
                         on_submit_click,
                         "submit",
                         "Submit")

def create_radio(parent, module, object_name, text=""):
    """Create the radio button object w/specified parametrs."""\
    # Create the radio button object
    radio = QRadioButton(text, parent)
    # Set the name for reference in style sheet
    radio.setObjectName(object_name)
    # Connect the button object to a module
    radio.clicked.connect(module)

    return radio

def create_temp_preference(parent, state_change):
    """Create the radio buttons Celsius and Fahrenheit to click temperature output."""
    fahrenheit = create_radio(parent, state_change, "f-temp", "Fahrenheit")
    celsius = create_radio(parent, state_change, "c-temp", "Celsius")

    # Put the radio buttons into one group
    temp_group = QButtonGroup(parent)
    temp_group.addButton(fahrenheit, 0)
    temp_group.addButton(celsius, 1)

    # Send the index of radio button to state_change()
    temp_group.idClicked.connect(state_change)

    # Fahrenheit is selected by default
    fahrenheit.setChecked(True)

    return fahrenheit, celsius