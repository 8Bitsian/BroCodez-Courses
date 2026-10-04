# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Third party imports
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

def create_layout(parent, widgets):
    """
    Create a layout manager for the widgets.

    Widgets order:
        0 - title label
        1 - api key textbox
        2 - city name textbox
        3 - submit button
        4 - temperature label
        5 - fahrenheit radio button
        6 - celsius radio button
        7 - weather icon
        8 - caption label
    """
    # Create basic vertical layout manager
    vbox = QVBoxLayout()
    vbox.setAlignment(Qt.AlignTop)
    vbox.setSpacing(12)

    # Create title label object
    widgets["title"].setAlignment(Qt.AlignCenter)
    vbox.addWidget(widgets["title"])

    # Create api key textbox object
    vbox.addWidget(widgets["api_key"])
    # Create city name textbox object
    vbox.addWidget(widgets["city_name"])

    # Create submit button object
    vbox.addWidget(widgets["submit"])

    # Create temperature label object
    widgets["temperature"].setAlignment(Qt.AlignCenter)
    vbox.addWidget(widgets["temperature"])

    # Create temperature unit radio buttons
    hbox = QHBoxLayout()
    hbox.setAlignment(Qt.AlignCenter)
    hbox.addWidget(widgets["fahrenheit"])
    hbox.addWidget(widgets["celsius"])
    vbox.addLayout(hbox)

    # Create weather icon picture object
    vbox.addWidget(widgets["picture"], alignment=Qt.AlignCenter)

    # Create caption label object
    widgets["caption"].setAlignment(Qt.AlignCenter)
    vbox.addWidget(widgets["caption"])

    # Set the layout manager to organize window
    parent.setLayout(vbox)

    return vbox