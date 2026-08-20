# 

# Note: Capitalize classes for better readability
class Car:
    # The constructor method is like a function
    # Use the initialization method to create the constructor w/attributes
    # The `self` keyword refers to the classes it is within
    def __init__(self, model, year, color, name, group):
        # To create the attributes, reference the `self` keyword and the parameters passed into the initialization method
        self.model = model
        self.year = year
        self.color = color
        self.name = name
        self.group = group

    # Method are actions that objects can perform
    def drive(self):
        print(f"You drive as a {self.year} {self.model}.")

    def park(self):
        print(f"You have a {self.color} paint coat.")

    def transform(self):
        print(f"You transform into {self.name}.")