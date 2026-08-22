# Static Methods
# Methods that belong to individual objects from classes are instance methods.
# Instance methods are best for operations on instances of the class (objects).
# EX. def get_info(self): return f"{self.name} = {self.position}"

# Static methods belong to a class rather than any object from that class (instance). Usually used for general utility functions.
# Static methods are best used for utility functiuons that do not need access to class data.
# EX. @staticmethod def km_to_mi(kilometers): return kilometers * 0.621371

class Employee:
    # Class Variables
    # Constructor/Initialization Method
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance Method: Methods that belong to individual objects from classes
    # Each object that gets created will have their own get_info instance
    def get_info(self):
        return f"{self.name} = {self.position}"

    # Static Method: Methods that belong to individal classes
    # To create a static method, you need to use the decorator `@staticmethod`
    @staticmethod
    # Static methods don't have self keyword since they aren't workign with the object created from the class
    def is_valid_pos(position):
        valid_pos = ["Administrator", "Developer", "IT Specialist", "Engineer"]
        return position in valid_pos