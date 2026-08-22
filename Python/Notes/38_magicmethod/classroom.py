# Magic (Dunder) Method
# Dunder methods (double underscore `__`) including `__init__`, `__str__`, `__eq__`, etc.
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects.

class Student:
    # Constructor/Initialization Method
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name} GPA: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa