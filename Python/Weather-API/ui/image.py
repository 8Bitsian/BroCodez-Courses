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

def get_image_path(filename, theme="light"):
    """Return the path to an image in the selected theme folder."""
    return IMAGE_DIR / theme / filename

def load_icon(filename, theme="light"):
    """Load an .svg file for the window/application icon"""
    icon_path = get_image_path(filename, theme)
    icon = QIcon(str(icon_path))

    if icon.isNull():
        print(f"Could not load icon: {icon_path}")

    return icon

def create_picture(parent, filename="cloud-drizzle.svg", theme="light"):
    """Create an SVG weather image widget."""
    picture = QSvgWidget(parent)
    picture.setObjectName("weatherIcon")
    picture.setFixedSize(QSize(150, 150))

    update_picture(picture, filename, theme)
    
    return picture

def update_picture(picture, filename, theme="light"):
    """Update the SVG file displayed by the weather image widget."""
    image_path = get_image_path(filename, theme)

    if not image_path.exists():
        print(f"Could not find image: {image_path}")
        return False

    loaded = picture.load(str(image_path))

    if not loaded:
        print(f"Could not load SVG: {image_path}")
        return False

    return True