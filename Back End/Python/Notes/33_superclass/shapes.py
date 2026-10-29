class Shapes:
    # In programming, we try not to repeat ourselves, therefore we move all shared variables into the superclass (parent class) since it will be inherited. This aides with readability and modularity.
    def __init__(self, name, color, is_filled,):
        self.name = name
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"The {self.name} is {self.color} and {"filled\n" if (self.is_filled) else "not filled\n"}")

class Circle(Shapes):
    def __init__(self, name, color, is_filled, radius):
        # To access the attributes within the superclass, use the super() method with the initialization method and a attribute list
        super().__init__(name, color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"The {self.name} area is {3.14 * self.radius * self.radius}cm²")
        print(f"The radius is {self.radius}cm")
        super().describe()

class Square(Shapes):
    def __init__(self, name, color, is_filled, width):
        super().__init__(name, color, is_filled)
        self.width = width
    
    def describe(self):
        print(f"The {self.name} area is {self.width * self.width}cm²")
        print(f"The width is {self.width}cm")
        super().describe()

class Triangle(Shapes):
    def __init__(self, name, color, is_filled, width, height):
        super().__init__(name, color, is_filled)
        self.width = width
        self.height = height
    
    def describe(self):
        print(f"The {self.name} area is {self.width * self.height / 2}cm²")
        print(f"The width is {self.width}cm")
        print(f"The height is {self.height}cm")
        super().describe()