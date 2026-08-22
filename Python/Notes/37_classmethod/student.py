# A class method allows operations related to the class itself.
# The keyword `self` refers to any object made within the class.
# The keyword `cls` refers to the class itself, and must be passed as the first parameter like the `self` keyword.

class Student:
    # Class Variables
    count = 0
    total_gpa = 0

    # Constructor/Initialization Method
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        # Whenever a student object is created, the count will increment by 1
        Student.count += 1
        # Whenever a student object is created, the total gpa will increment by their gpa
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # To create a class method, utilize the class method decorator `@classmethod` and pass in the class keyword `cls` as the first parameter.
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if (cls.count == 0):
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"