# pyQt5 CSS Style Sheets
# The pyQt5 GUI has an embedded module for developing cascading style sheets (or CSS)

# Standard-library imports
import sys
# Third-party or local library imports
from styles import MainWindow
from PyQt5.QtWidgets import QApplication

# Runs the main program
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()