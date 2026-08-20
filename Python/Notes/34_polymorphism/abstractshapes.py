from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Pizza(Circle):
    def __init__(self, name, radius, topping):
        super().__init__(name, radius)
        self.topping = topping

class Square(Shape):
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def area(self):
        return self.length ** 2

class Triangle(Shape):
    def __init__(self, name, base, height):
        self.name = name
        self.base = base
        self.height = height
        
    def area(self):
        return (self.base * self.height) / 2

