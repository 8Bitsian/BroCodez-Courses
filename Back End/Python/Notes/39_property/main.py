# Property
# The @property decorator is used to define a method as a property (which can be accessed like an attribute). It can add additional logic to read, write, or delete attributes. Gives a getter, setter, and deleter method

import shapes

def main():
    rectangle = shapes.Rectangle(name="rectangle", color="WHITE", is_filled=False, width=3, length=4)

    print(rectangle)            # Prints "<shapes.Rectangle object at 0x00000236BCD4C830>"

    rectangle.describe()        # Prints "The rectangle is WHITE and not filled"

    # By using the underscore you can access private or internal variables
    print(f"The current width is {rectangle._width}cm")     # Prints "3"
    print(f"The current length is {rectangle._length}cm\n")    # Prints "4"

    rectangle.width = 6         # Prints "The new width has been set..."
    print(rectangle.width)      # Prints "The width is 6.0cm"

    rectangle.length = 7        # Prints "The new length has been set..."
    print(rectangle.length)     # Prints "The length is 7.0cm"

    rectangle.describe()        # Prints "The rectangle is WHITE and not filled"

    del rectangle.width         # Prints "The width was deleted..."
    # print(rectangle.width)    # "AttributeError: 'Rectangle' object has no attribute 'width'"
    del rectangle.length        # Prints "The length was deleted..."

if __name__ == "__main__":
    main()