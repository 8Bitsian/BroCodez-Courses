# pyQt5 CSS Style Sheets
# The pyQt5 GUI has an embedded module for developing cascading style sheets (or CSS)

# The `QMainWindow` module is designed for creating the main application window

from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QHBoxLayout
# The `QIcon` module is designed to work with images
from PyQt5.QtGui import QIcon
# The `Qt` module is used for alignments
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    # Constructor/Initialization Method
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyQt5 GUI CSS Styles")
        self.setWindowIcon(QIcon(r"Python\Notes\47_cssstyles\icon.png"))

        # Initialize button objects
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        # Call initUI() method
        self.initUI()

    def initUI(self):
        # Create the central widget to apply the layout manager to
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the layout manager
        hbox = QHBoxLayout()

        # Create the buttons
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # Apply the horizontal layout manager to the central widget container
        central_widget.setLayout(hbox)

        # Set an object name to reference the button objects when applying style properties.
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Rather than apply css style properties individually, we can use the `setStyleSheet()` once by appending it to the window object itself (i.e., using the `self` object).
        # Because you'll likely need to write a lot of css, use tripple quotes which are used to write very long strings in a more organized manner.
        # You can use classes as well to write css style code.
        self.setStyleSheet("""
            QPushButton{
                font-family: Jetbrains Mono;
                font-weight: bold;
                font-size: 40px;
                padding: 15px 75px;
                margin: 15px;
                border: 3px solid;
                border-radius: 5px;
                background-color: gray
            }

            QPushButton#button1:hover{
                background-color: cyan;
            }

            QPushButton#button2:hover{
                background-color: magenta;
            }

            QPushButton#button3:hover{
                background-color: yellow;
            }

        """)
