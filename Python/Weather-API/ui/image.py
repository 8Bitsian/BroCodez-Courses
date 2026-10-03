# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Standard-library imports
from pathlib import Path

# Third-party imports
from PyQt5.QtGui import QIcon

# Global Variables
PROJECT_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = PROJECT_DIR / "images" 

def load_icon(filename):
    """Load the window icon for an .svg file image"""

    icon_path = IMAGE_DIR / filename
    icon = QIcon(str(icon_path))

    if icon.isNull():
        print(f"Could not load icon: {icon_path}")

    return icon