# pyQt5 GUI Labels

# Third-party or local library imports
# Widgets are the building blocks of any PyQt5 application.
# They begin with `Q` to help distinguish them from other libraries widgets.
# The `QLabel` module is designed for creating text labels
from PyQt5.QtWidgets import QLabel
# The `QFont` module is designed to work with text and change fonts
from PyQt5.QtGui import QFont
# The `Qt` module is used for alignments
from PyQt5.QtCore import Qt

def create_title(parent):
    # To create a text label within the window, create a label object within the constructor/initialization method using the `QLabel()` method and pass in a string and self as parameters.
    text = "8BitSoftware"
    title = QLabel(text, parent)

    # To adjust the height and width of the label, use the `setGeometry()` method and pass in the following parameters: `aw` (width) and `ah` (height)
    title.setGeometry(0, 0, 500, 500)

    # To stylize the label, you can change the font, size, and weight of the label using the `setFont(QFont())` method by passing in the font name as a string and font size and weight in pixels. The weights are as follows: Thin = 100, ExtraLight = 200, Light = 300, Regular = 400, Medium = 500, Semibold = 600, Bold = 700, ExtraBold = 800
    title.setFont(QFont("JetBrains Mono", 35, 600))

    # To further stylize the label, you can use a style sheet similar to CSS, using the `setStyleSheet()` method and pass in arguments like you would in CSS.
    # when passing in a color argument, you can either use keywords, such as `purple`, or hexadecimal or rgb values, such as `#FFFFF0`.
    title.setStyleSheet("color: #8C52FF;"
                            "background-color: #FFFFF0;"
                            "font-weight: semibold;"
                            "font-style: italic;"
                            "text-decoration: underline")

    # To align the text label within the window, use the `setAlignment()` method. You can set the alignment both vertically and horizontally, use the bitwise operator OR `|`.
    title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)         # Center & Top
    # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)    # Center & Bottom
    # label.setAlignment(Qt.AlignCenter)                      # center

    return title

def color_title(parent):
    # When you create label objects, they are automatically overlapping.
    # To create multiple of the same text labels, utilize a 1D array and a for loop
    labels = []

    for number, color in enumerate(["magenta", "cyan", "yellow", "tan", "black"]):
        label = QLabel(f"#{number}", parent)
        label.setStyleSheet(f"background-color: {color};")
        labels.append(label)

    return labels