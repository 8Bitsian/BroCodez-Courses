# Polymorphism
# Polymorphism is a greek word that means "to mhave many forms or faces" with poly meaning "many" and morphe meaning "form".

# There are two ways to achieve polymorphism:
# 1. Inheritance: An object coult could be treated of the same type as a parent class
# 2. "Duck typing": Object must have necessary attributes/methods

import abstractshapes

def name():
    pass

def main():
    circle = abstractshapes.Circle(name="Circle", radius=5)
    square = abstractshapes.Square(name="Square", length=5)
    triangle = abstractshapes.Triangle(name="Triangle", base=5, height=6)
    pizza = abstractshapes.Pizza(name="Pizza", topping="cheese", radius=5)

    shapes = [circle, square, triangle, pizza]
    for shape in shapes:
        print(f"{shape.name}'s area is {shape.area()} cm²")

if __name__ == "__main__":
    # print(f"Called main.py file is: {__name__}\n")
    main()
    # print("Exiting main.py file...")