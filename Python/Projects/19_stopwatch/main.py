"""
Project 19: PyQt5 Digital Stopwatch Program
Notes: 46 and 47 for PyQt5
Description: Create a digital stopwatch program utilizing the PyQt5 GUI
"""

# Standard-library imports
import sys, os
# Third-party or local library imports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream
from ui.window import MainWindow

# Load the QSS Style sheet
def load_stylesheet(app,filepath):
    file = QFile(filepath)
    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())
    else:
        print(f"Could not load stylesheet: {filepath}")

# Run the main program
def main():
    # Ensure app can find resources
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    app = QApplication(sys.argv)

    load_stylesheet(app, 'css/style.qss')

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    print(f"Running {__name__}\n")
    main()
    print("Program finished.")