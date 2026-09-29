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

def create_layout(parent, button, checkbox, labels, title, picture):
    # To align widgets/labels use the various box layout managers:
    # To create a vertical layout manager object via the `QVBoxLayout()` method
    # vbox = QVBoxLayout()
    # To create a horizontal layout manager object via the `QHBoxLayout()` method
    # hbox = QHBoxLayout()
    # To create a grid layout manager object via the `QGridLayout()` method
    grid = QGridLayout(parent)

    # Use the `addWidget()` method to insert a label object. For grid specifically, we have to specify a row and column after the label.
    title.setAlignment(Qt.AlignCenter)
    grid.addWidget(title, 0, 0, 1, 2)
    grid.addWidget(picture, 1, 0, 1, 2)
    grid.addWidget(button, 2, 0, 1, 2)
    grid.addWidget(checkbox, 3, 0, 1, 2)

    # To add mutliple widgets utilize a for loop
    for index, label in enumerate(labels):
        grid.addWidget(label, (4 + index // 2), (index % 2))

    # To show the layout use the `setLayout()` method and pass in the layout manager object
    # central_widget.setLayout(grid)

    return grid