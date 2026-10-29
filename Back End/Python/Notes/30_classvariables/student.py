class Student:
    # Class variables are shared among all instances (objects) of a class.
    # They are defined outside of the constructor method.
    class_year = 2026
    num_students = 0

    # Constructor/initialization method
    # The `self` keyword refers to the object that is being referenced
    # Each objects has an instance variable, i.e., their attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Create a counter variable to count how many objects (students) are being created via accessing the Class name and using a class variable.
        Student.num_students += 1