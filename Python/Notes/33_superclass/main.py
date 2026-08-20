# Superclass
# The `super()` function is used in a child class (subclass) to call methods from a parent class (superclass). It allows you to extend the functionality of the inherited methods.

import shapes

def main():
    circle = shapes.Circle(name="circle", color="RED", is_filled=True, radius=5)
    square = shapes.Square(name="square", color="GREEN", is_filled=False, width=6)
    triangle = shapes.Triangle(name="triangle", color="BLUE", is_filled=True, width=3, height=4)

    circle.describe()
    square.describe()
    triangle.describe()

if __name__ == "__main__":
    main()