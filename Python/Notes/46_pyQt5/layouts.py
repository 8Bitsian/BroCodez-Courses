# pyQt5 GUI Layout Managers

# Third-party or local library imports
# Widgets are the building blocks of any PyQt5 application.
# They begin with `Q` to help distinguish them from other libraries widgets.
# The `QVBoxLayout` module is designed for the vertical box layout
# The `QHBoxLayout` module is designed for the horizontal box layout
# The `QGridLayout` module is designed for the grid box layout
from PyQt5.QtWidgets import (QVBoxLayout,
                             QHBoxLayout,
                             QGridLayout)
# The `Qt` module is used for alignments
from PyQt5.QtCore import Qt

def create_layout(parent, button, radios, checkbox, textbox, submit_button, labels, title, picture):
    # To align widgets/labels use the various box layout managers:
    # To create a vertical layout manager object via the `QVBoxLayout()` method
    l_group = QVBoxLayout()
    r_group = QVBoxLayout()

    # To create a horizontal layout manager object via the `QHBoxLayout()` method
    hbox = QHBoxLayout()

    # To create a grid layout manager object via the `QGridLayout()` method
    grid = QGridLayout(parent)

    # Use the `addWidget()` method to insert a label object. For grid specifically, we have to specify a row and column after the label.
    title.setAlignment(Qt.AlignCenter)
    grid.addWidget(title, 0, 0, 1, 2)
    grid.addWidget(picture, 1, 0, 1, 2)
    grid.addWidget(button, 2, 0, 1, 2)

    # Two radio buttons per row, starting at row 3
    for radio in radios[:3]:
        l_group.addWidget(radio)
    for radio in radios[3:]:
        r_group.addWidget(radio)
    grid.addLayout(l_group, 3, 0)
    grid.addLayout(r_group, 3, 1)

    grid.addWidget(checkbox, 4, 0, 1, 2)

    hbox.addWidget(textbox, 1)
    hbox.addWidget(submit_button)
    grid.addLayout(hbox, 5, 0, 1, 2)

    # To add mutliple widgets utilize a for loop
    for index, label in enumerate(labels):
        grid.addWidget(label, (6 + index // 2), (index % 2))

    # To show the layout use the `setLayout()` method and pass in the layout manager object
    # central_widget.setLayout(grid)

    return grid