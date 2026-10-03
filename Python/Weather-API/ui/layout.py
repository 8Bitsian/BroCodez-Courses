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
        1 - textbox line edit
        2 - submit button
        3 - temperature label
        4 - fahrenheit radio button
        5 - celsius radio button
        6 - weather icon
        7 - caption label
    """

    vbox = QVBoxLayout()
    vbox.setAlignment(Qt.AlignTop)

    # title
    widgets[0].setAlignment(Qt.AlignCenter)
    vbox.addWidget(widgets[0])

    # textbox
    widgets[1].setAlignment(Qt.AlignCenter)
    vbox.addWidget(widgets[1])

    # s_button
    vbox.addWidget(widgets[2])

    # temperature
    widgets[3].setAlignment(Qt.AlignCenter)
    vbox.addWidget(widgets[3])

    # radio buttons
    hbox = QHBoxLayout()
    hbox.setAlignment(Qt.AlignCenter)
    # f_button & c_button
    hbox.addWidget(widgets[4])
    hbox.addWidget(widgets[5])
    vbox.addLayout(hbox)

    # picture
    vbox.addWidget(widgets[6], alignment=Qt.AlignCenter)

    # caption
    widgets[7].setAlignment(Qt.AlignCenter)
    vbox.addWidget(widgets[7])

    # Set the layout manager to organize window
    parent.setLayout(vbox)

    return vbox