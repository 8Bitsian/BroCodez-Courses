# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Standard-library imports
import sys
from pathlib import Path

# Third-party imports
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

# Local library imports
from ui.window import MainWindow

# Global variables
BASE_DIR = Path(__file__).resolve().parent

COLORS = {
    "BRICK_EMBER": "#B80C09",
    "YALE_BLUE": "#0B4F6C",
    "BRIGHT_SKY": "#01BAEF",
    "GHOST_WHITE": "#FBFBFF",
    "INK_BLACK": "#040F16"
}

# Load the fonts
def load_fonts():
    """Load the application fonts."""
    font_dir = BASE_DIR / "fonts"

    for font_path in font_dir.glob("*.ttf"):
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        if font_id == -1:
            print(f"Could not load font: {font_path}")

# Load the QSS Style sheet
def load_stylesheet(app, file_path):
    """Load the style sheet and replace color keywords."""
    file_path = BASE_DIR / "css" / "light.qss"
    file = QFile(str(file_path))

    if not file.open(QFile.ReadOnly | QFile.Text):
        print(f"Could not load stylesheet: {file_path}")
        return

    stylesheet = QTextStream(file).readAll()
    file.close()

    for color_name, hex_color in COLORS.items():
        stylesheet = stylesheet.replace(f"{{{{{color_name}}}}}", hex_color)
    
    app.setStyleSheet(stylesheet)

# Run the main program
def main():
    """Final Project: A Weather API Application that gets API data to show real-time weather."""
    app = QApplication(sys.argv)

    load_fonts()
    load_stylesheet(app, BASE_DIR / "css" / "light.qss")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    print(f"Running {__name__}\n")
    main()
    print("Program finished.")