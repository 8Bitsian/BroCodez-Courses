# pyQt5 GUI

# Standard-library imports
import sys # The `sys` or system module provides access to system-specific parameters and functions

# Third-party or local library imports
# Install Pyqt5 library via the termianl w/the following command: `pip install PyQt5`. Be sure to use the proper capitalization when calling this library.

# Widgets are the building blocks of any PyQt5 application. They begin with `Q` to help distinguish them from other libraries widgets.
# The `QMainWindow` module is designed for creating the main application window
from PyQt5.QtWidgets import QMainWindow
# The `QIcon` module is designed to work with images
from PyQt5.QtGui import QIcon

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