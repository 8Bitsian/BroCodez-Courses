# pyQt5 GUI

# Standard-library imports
import sys # The `sys` or system module provides access to system-specific parameters and functions

# Third-party or local library imports
# Install Pyqt5 library via the termianl w/the following command: `pip install PyQt5`. Be sure to use the proper capitalization when calling this library.

# Widgets are the building blocks of any PyQt5 application. They begin with `Q` to help distinguish them from other libraries widgets.
# The `QMainWindow` module is designed for creating the main application window
# The `QLabel` modulke is designed for creating text labels
from PyQt5.QtWidgets import QMainWindow, QLabel

# The `QIcon` module is designed to work with images
# The `QFont` module is designed to work with text and change fonts
from PyQt5.QtGui import QIcon, QFont

# The `Qt` module is used for alignments
from PyQt5.QtCore import Qt

# By inheriting from the parent class of `QMainWindow`, we can customize our own windows to display to the end user via a child class.
class MainWindow(QMainWindow):
    # Constructor/Initialization Method
    def __init__(self):
        super().__init__()
        # To set the title for the window, use the `setWindowTitle()` method and pass in a string
        self.setWindowTitle("My First GUI")
        # To set where the window appears and the inital size of the window, use the `setGeometry()` method and pass in the following parameters: `ax` = x-coordinate, `ay` = y-coordinate, `aw` = width of window, and `ah` = height of window. All of the parameters are measured in pixels
        # If the `ax` and `ay` parameters are set to `0` then the window will appear in the top-right corner of the screen.
        # self.setGeometry(ax=0, ay=0, aw=500, ah=500)
        self.setGeometry(700, 300, 500, 500)
        # To set the icon for the window, use the `setWidnowIcon()` method and pass in the `QIcon()` method with a file path to the image you'd like to use
        self.setWindowIcon(QIcon(r"Python\Notes\46_pyQt5\icon.png"))

        # To create a test label within the window, create label object within the constructor/initialization method using the `QLabel()` method and pass in a string and the self paramters
        title = "8BitSoftware"
        label = QLabel(title, self)

        # To the height and width of the label, use the `setGeometry()` method and pass in the following parameters: `aw` = width of label, and `ah` = height of label
        label.setGeometry(0, 0, 500, 500)

        # To change the font and size of the label use the `setFont(QFont())` method and pass in the font name as a string, the font size in pixels, and font weight in pixels as the paramters
        # Thin = 100, ExtraLight = 200, Light = 300, Regular = 400, Meidum = 500, Semibold = 600, Bold = 700, ExtraBold = 800
        label.setFont(QFont("JetBrains Mono", 35, 600))
        
        # To insert a style sheet similar to CSS, use the `setStyleSheet()` method and pass in arguments like in CSS
        # when passing in a color argument, you can either use keywords, such as purple, or hexadecimal or rgb values
        label.setStyleSheet("color: #8C52FF;"
                            "background-color: #FFFFF0;"
                            "font-weight: semibold;"
                            "font-style: italic;"
                            "text-decoration: underline")
        
        # To align the text label within the window, use the `setAlignment()` method
        # Use `Qt.AlignTop` to align the label to the vertical top of the window
        # label.setAlignment(Qt.AlignTop)
        # Use `Qt.AlignVCenter` to align the label to the vertical center of the window
        # label.setAlignment(Qt.AlignVCenter) 
        # Use `Qt.AlignBottom` to align the label to the vertical bottom of the window
        # label.setAlignment(Qt.AlignBottom) 

        # Use `Qt.AlignRight` to align the label to the horizontal right of the window
        # label.setAlignment(Qt.AlignRight)
        # Use `Qt.AlignHCenter` to align the label to the horizontal center of the window
        # label.setAlignment(Qt.AlignHCenter) 
        # Use `Qt.AlignLeft` to align the label to the horizontal left of the window
        # label.setAlignment(Qt.AlignLeft)

        # To set the alignment both vertically and horizontally, use the bitwise operator OR `|` to combine the two flags.
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)         # Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)    # Center & Bottom

        # To center the label in the middle of the winow simply use `Qt.AlignCenter`
        # label.setAlignment(Qt.AlignCenter)