class Shapes:
    # Constructor/Initialization Method
    def __init__(self, name, color, is_filled,):
        self.name = name
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"The {self.name} is {self.color} and {"filled" if (self.is_filled) else "not filled"}")

class Rectangle(Shapes):
    def __init__(self, name, color, is_filled, width, length):
        super().__init__(name, color, is_filled)
        # Prefixing attributes w/underscore implies that they are private
        # meaning they are internal and shouldn't be accessed directly by the end user
        self._width = width
        self._length = length

    def describe(self):
        super().describe()
        print(f"The {self.name} area is {self._width * self._length}cm²\n")

    # To get access to private attributes, create getter methods via the @property decorator
    # You have to include the underscore when referencing private attributes
    @property
    def width(self):
        # @tealeaffreeleaf on Twitch for reminding me that returns exist
        return f"The width is {self._width:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
            print("The new width has been set...")
        else:
            raise ValueError("ERROR: Invalid Input - Width must be greater than zero.")

    @width.deleter
    def width(self):
        del self._width
        print("The width was deleted...")

    @property
    def length(self):
        return f"The length is {self._length:.1f}cm"

    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self._length = new_length
            print("The new length has been set...")
        else:
            raise ValueError("ERROR: Invalid Input - Length must be greater than zero.")

    @length.deleter
    def length(self):
        del self._length
        print("The length was deleted...")