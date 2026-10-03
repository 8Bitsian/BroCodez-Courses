# Final Project: Weather API Application
# Description: A weather app that gets API data to show real-time weather.

# Standard-library imports
from pathlib import Path

# Third-party imports
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtSvg import QSvgWidget

# Global Variables
PROJECT_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = PROJECT_DIR / "images" 

# Global Collections
WEATHER_IMAGES = {
    "Clear": "sun.svg",
    "Clouds": "cloud.svg",
    "Rain": "cloud-rain.svg",
    "Thunderstorm": "cloud-lightning.svg",
    "Snow": "cloud-snow.svg",
}

def load_icon(filename):
    """Load an .svg file for the window/application icon"""
    icon_path = IMAGE_DIR / filename
    icon = QIcon(str(icon_path))

    if icon.isNull():
        print(f"Could not load icon {image_path}")

    return icon

def create_picture(parent, filename="cloud-drizzle.svg"):
    """Create an SVG weather image widget."""
    picture = QSvgWidget(parent)
    picture.setObjectName("weatherIcon")
    picture.setFixedSize(QSize(150, 150))

    update_picture(picture, filename)

    return picture

def update_picture(picture, filename):
    """Update the SVG file displayed by the weather image widget."""
    image_path = IMAGE_DIR / filename

    if not image_path.exists():
        print(f"Could not find image: {image_path}")
        return

    picture.load(str(image_path))