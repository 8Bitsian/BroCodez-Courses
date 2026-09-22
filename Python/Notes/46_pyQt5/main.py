# pyQt5 GUI
# A built-in python Graphical User Interface (GUI)

# Standard-library imports
import sys # The `sys` or system module provides access to system-specific parameters and functions
# Third-party or local library imports
from window import MainWindow
# Install Pyqt5 library via the termianl w/the following command: `pip install PyQt5`. Be sure to use the proper capitalization when calling this library.
# Widgets are the building blocks of any PyQt5 application. They begin with `Q` to help distinguish them from other libraries widgets.
from PyQt5.QtWidgets import QApplication
# The `QApplication` module manages the GUI app's control flow and main settings

# Runs the main program
def main():
    # create an app object via the `QApplication` module and pass in the singluar argument of `sys.argv` which allows PyQt5 to process any command line arguments intended for it if we use command prompt or terminal.
    app = QApplication(sys.argv)
    # When creating a window object, the default behavior is to hide it.
    window = MainWindow()   # Prints ""
    # To output the window access the `show()` method
    window.show()   # This will show the window for a brief moment
    # To prolong it until we either interact or close it, use the `sys.exit()` method and pass in the application object which has a built-in `exec_()` execute method
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()