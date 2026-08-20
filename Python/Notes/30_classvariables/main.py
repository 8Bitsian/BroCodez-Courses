# Class Variables

# Class variables are shared among all instances (objects) of a class.
# They are defined outside of the constructor method.
from student import Student

def graduation(student):
    print(f"The graduating class of {student.class_year} has {student.num_students} students.\n")

def main():
    # Create Student objects
    student1 = Student("Charlie", 25)
    student2 = Student("Steven", 26)
    student3 = Student("Rachel", 23)
    student4 = Student("Timothy", 27)

    # Access instance variables via their specific object
    print(student1.name)        # Prints "Charlie"
    print(student1.age)         # Prints "25"
    print(student2.name)        # Prints "Steven"
    print(f"{student2.age}\n")         # Prints "26"

    # It's good practice to access a class variables by the name of their class
    print(Student.class_year)   # Prints "2026"
    print(f"{Student.num_students}\n") # Prints "3"

    graduation(student1)

if __name__ == "__main__":
    main()