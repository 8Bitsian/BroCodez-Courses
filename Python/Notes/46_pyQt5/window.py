# pyQt5 GUI

# Standard-library imports
import sys # The `sys` or system module provides access to system-specific parameters and functions

# Third-party or local library imports
# Install Pyqt5 library via the termianl w/the following command: `pip install PyQt5`. Be sure to use the proper capitalization when calling this library.

# Widgets are the building blocks of any PyQt5 application. They begin with `Q` to help distinguish them from other libraries widgets.
# The `QMainWindow` module is designed for creating the main application window
# The `QLabel` module is designed for creating text labels
# The `QWidget` module is designed for being the basic container
# The `QVBoxLayout` module is designed for the vertical box layout
# The `QHBoxLayout` module is designed for the horizontal box layout
# The `QGridLayout` module is designed for the grid box layout
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

# The `QIcon` module is designed to work with images
# The `QFont` module is designed to work with text and change fonts
# The `QPixmap` module is designed to handle images and provides functionality for loading, manipulating, and displaying images.
from PyQt5.QtGui import (QIcon, QFont, QPixmap)

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
        # To set the icon for the window, use the `setWindowIcon()` method and pass in the `QIcon()` method with a file path to the image you'd like to use
        self.setWindowIcon(QIcon(r"Python\Notes\46_pyQt5\icon.png"))

        # Call the `initUI()` function from within the initialization method.
        self.initUI()

        # To create a test label within the window, create label object within the constructor/initialization method using the `QLabel()` method and pass in a string and the self paramters
        text_1 = "8BitSoftware"
        title = QLabel(text_1, self)

        # To the height and width of the label, use the `setGeometry()` method and pass in the following parameters: `aw` = width of label, and `ah` = height of label
        title.setGeometry(0, 0, 500, 500)

        # To change the font and size of the label use the `setFont(QFont())` method and pass in the font name as a string, the font size in pixels, and font weight in pixels as the paramters
        # Thin = 100, ExtraLight = 200, Light = 300, Regular = 400, Meidum = 500, Semibold = 600, Bold = 700, ExtraBold = 800
        title.setFont(QFont("JetBrains Mono", 35, 600))
        
        # To insert a style sheet similar to CSS, use the `setStyleSheet()` method and pass in arguments like in CSS
        # when passing in a color argument, you can either use keywords, such as purple, or hexadecimal or rgb values
        title.setStyleSheet("color: #8C52FF;"
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
        title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)         # Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)    # Center & Bottom
        # To center the label in the middle of the winow simply use `Qt.AlignCenter`
        # label.setAlignment(Qt.AlignCenter)

        # To create a picture label within the window, create label object within the constructor/initialization method using the `QLabel()` method and pass in a `self` paramter
        picture = QLabel(self)
        # To the height and width of the label, use the `setGeometry()` method and pass in the following parameters: `aw` = width of label, and `ah` = height of label
        picture.setGeometry(0, 0, 250, 250)

        # To create the image label object use the `QPixmap()` method and pass in a string of the relative file path to the image you would like to use. This alone will not show the image in the window.
        pixmap = QPixmap(r"Python\Notes\46_pyQt5\icon.png")

        # To show the image, you have to set it to the picture label via the `setPixmap()` method and pass in the pixmap object to the label object.
        picture.setPixmap(pixmap)

        # To scale the image to the size of the label, use the `setScaledContents()` method and pass in the boolean value of `True`
        picture.setScaledContents(True)

        # To align the image, use the `setGeometry()` method and utilzie the `label.width()` and `label.height()` methods to reflect the current value for the image. The following parameters (`aw` = width of label, and `ah` = height of label) can be changed to chnage the justification (alignment) of the image:
        # `aw = (self.width() - picture.width()) // 2` | Horizontal Center
        # `aw = self.width() - picture.width()` | Horizontal Right
        # `aw = 0` | Horizontal Left
        # `ah = (self.height() - picture.height()) // 2` | Vertical Center
        # `ah = self.height() - picture.height()` | Veritcal Bottom
        # `ah = 0` | Veritcal Top

        picture.setGeometry((self.width() - picture.width()) // 2,     # horizontal center
                            (self.height() - picture.height()) // 2,   # vertical center
                            picture.width(),
                            picture.height())

        # When creating the user interface define another Constructor/Initialization Method using the keyword `initUI()` and pass the `self` parameter

        # MainWindow() cannot utilize a layout manager (e.g., `QWidget`, `QVBoxLayout`, `QHBoxLayout`, and `QGridLayout`) since it has a layout structure that is incompatible.abs
        # To create a UI, you have to create a widget and add a layout manager to the main window to display the layout.
    def initUI(self):
        # Create a generic widget called `central_widget`
        central_widget = QWidget()
        # Use the `setCentralWidget()` method to create a central widget object to apply the layout manager to the main window
        self.setCentralWidget(central_widget)

        # When you create label objects, they are automatically overlapping.
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: magenta;")
        label2.setStyleSheet("background-color: cyan;")
        label3.setStyleSheet("background-color: yellow;")
        label4.setStyleSheet("background-color: tan;")
        label5.setStyleSheet("background-color: black;")

        # To align the labels vertically create a vertical layout manager object via the `QVBoxLayout()` method.
        # vbox = QVBoxLayout()

        # To align the labels horizontally create a vertical layout manager object via the `QHBoxLayout()` method.
        # hbox = QHBoxLayout()

        # To align the labels in a grid create a grid layout manager object via the `QGridLayout()` method.
        grid = QGridLayout()

        # Use the `addWidget()` method to insert a label object. For grid specifically, we have to specify a row and column after the label.
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 1, 1)
        grid.addWidget(label3, 2, 2)
        grid.addWidget(label4, 3, 3)
        grid.addWidget(label5, 4, 4)

        # To show the layout use the `setLayout()` method and pass in the layout manager object
        central_widget.setLayout(grid)