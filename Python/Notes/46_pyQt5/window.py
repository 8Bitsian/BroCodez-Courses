# pyQt5 GUI

# Third-party or local library imports
# Install Pyqt5 library via the terminal w/the following command: `pip install PyQt5`.
# Be sure to use the proper capitalization when calling this library.
# Widgets are the building blocks of any PyQt5 application.
# They begin with `Q` to help distinguish them from other libraries widgets.

# The `QMainWindow` module is designed for creating the main application window
# The `QWidget` module is designed for being the basic container
# The `QRadioButton` module is designed for creating radio buttons
from PyQt5.QtWidgets import QMainWindow, QWidget, QRadioButton
# The `QIcon` module is designed to work with images
from PyQt5.QtGui import QIcon
# The `Qt` module is used for alignments
from PyQt5.QtCore import Qt

from buttons import (create_button,
                     create_submission, create_radio_button)
from checkboxes import create_checkbox
from textboxes import create_textbox
from labels import create_title, color_title
from pictures import create_picture
from layouts import create_layout

# By inheriting from the parent class of `QMainWindow`, we can customize our own windows to display to the end user via a child class.
class MainWindow(QMainWindow):
    # Constructor/Initialization Method
    def __init__(self):
        super().__init__()

        # To set the title for the window, use the `setWindowTitle()` method and pass in a string
        self.setWindowTitle("My First GUI")

        # To set the initial position and size of the window, use the `setGeometry()` method and pass in the following parameters: `ax` (x-coordinate), `ay` (y-coordinate), `aw` (width), and `ah` (height). All of the parameters are measured in pixels. For example, if the `ax` and `ay` parameters are set to `0` then the window will appear in the top-right corner of the screen (Ex. `self.setGeometry(ax=0, ay=0, aw=500, ah=500)`).
        self.setGeometry(700, 300, 500, 500)

        # To set the icon for the window, use the `setWindowIcon()` method and pass in the `QIcon()` method with a relative file path to the image you'd like to use.
        self.setWindowIcon(QIcon(r"Python\Notes\46_pyQt5\icon.png"))

        # When creating the UI you'll have to define another initialization method using the keyword `initUI()` and pass the `self` parameter since the initial constructor cannot utilize a layout manager (e.g., `QWidget`, `QVBoxLayout`, `QHBoxLayout`, and `QGridLayout`) since it has a layout structure that is incompatible.

        # To create a UI, you have to create a widget and add a layout manager to the main window to display the layout. To create a generic widget, call the `QWidget()` method and don't pass in any parameters.
        central_widget = QWidget(self)
        # Use the `setCentralWidget()` method to create a central widget object to apply the layout manager to the main window
        self.setCentralWidget(central_widget)

        self.button = create_button(central_widget, self.on_button_click)
        self.radios = create_radio_button(central_widget, self.on_radio_click)
        
        self.checkbox = create_checkbox(central_widget, self.checkbox_changed)

        self.textbox = create_textbox(central_widget)
        self.submit_button = create_submission(central_widget, self.on_submit_click)

        labels = color_title(central_widget)
        title = create_title(central_widget)
        picture = create_picture(central_widget,
                                 r"Python\Notes\46_pyQt5\icon.png")
        
        create_layout(central_widget,
                      self.button,
                      self.radios,
                      self.checkbox,
                      self.textbox,
                      self.submit_button,
                      labels,
                      title,
                      picture)
    
    def on_button_click(self):
        print("Button Clicked!")
        # To change the text on the button after the end user clicks on it, use the `.setText()` method and pass in a string.
        self.button.setText("Clicked!")
        self.button.setStyleSheet("color: #8C52FF;"
                                  "background-color: #FFFFF0;"
                                  "font-style: italic;")
        # To disable buttons after clicking on them, call the `setDisabled()` method and pass in the boolean paramter `True`
        self.button.setDisabled(True)
        # self.label.setText("Goodbye!")

    def on_submit_click(self):
        print("Submit Clicked!")
        self.button.setStyleSheet("color: #8C52FF;"
                                  "background-color: #FFFFF0;"
                                  "font-style: italic;")
        
        text = self.textbox.text()
        print(f"You submitted: {text}")

    def on_radio_click(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected!")

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("Box Checked!")   # State is in 2
        else:
            print("Box Unchecked!") # State is in 0