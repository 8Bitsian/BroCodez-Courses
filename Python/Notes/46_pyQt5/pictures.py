# pyQt5 GUI Pictures

# Third-party or local library imports
# Widgets are the building blocks of any PyQt5 application.
# They begin with `Q` to help distinguish them from other libraries widgets.
# The `QLabel` module is designed for creating text labels
from PyQt5.QtWidgets import QLabel
# The `QPixmap` module is designed to handle images and provides functionality for loading, manipulating, and displaying images.
from PyQt5.QtGui import QPixmap

def create_picture(parent, image_path):
    # To create a label within the window, create a label object within the initialization method using the `QLabel()` method and pass in `self` as the paramter.
    picture = QLabel(parent)

    # To create the image object use the `QPixmap()` method and pass in a string of the relative file path to the image you would like to use. This alone will not show the image in the window. To show the image, you have to set it to the label via the `setPixmap()` method and pass in the pixmap object to the label object.
    # image_path = r"Python\Notes\46_pyQt5\icon.png"
    picture.setPixmap(QPixmap(image_path))

    # To scale the image to the size of the label, use the `setScaledContents()` method and pass in the boolean value of `True`
    picture.setScaledContents(True)

    # To define the size of the label, you can adjust the width and height using the `setFixedHeight()` method and pass in the following parameters: `aw` (width) and `ah` (height)
    picture.setFixedSize(250, 250)

    # To align the image, use the `setGeometry()` method and utilzie the `label.width()` and `label.height()` methods to reflect the current value for the image. The following parameters (`aw` = width of label, and `ah` = height of label) can be changed to chnage the justification (alignment) of the image:
    # `aw = (self.width() - picture.width()) // 2` | Horizontal Center
    # `aw = self.width() - picture.width()` | Horizontal Right
    # `aw = 0` | Horizontal Left
    # `ah = (self.height() - picture.height()) // 2` | Vertical Center
    # `ah = self.height() - picture.height()` | Veritcal Bottom
    # `ah = 0` | Veritcal Top

    # picture.setGeometry((self.width() - picture.width()) // 2,     # horizontal center
    #                     (self.height() - picture.height()) // 2,   # vertical center
    #                     picture.width(),
    #                     picture.height())

    return picture