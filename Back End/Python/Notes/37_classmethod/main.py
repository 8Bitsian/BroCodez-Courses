# Class Method
# A class method allows operations related to the class itself.
# Take (cls) as the first parameter, which represents the class itself.

# Instance methods: Best for operations on instances of the class (objects)
# Static methods: Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

from student import Student

def main():
    print(Student.get_count())  # Print "Total number of students: 0"
    print(Student.get_avg_gpa())    # Print "Total average gpa: 0"

    student1 = Student("Mark", 3.4)
    student2 = Student("Bob", 2.6)
    student3 = Student("Wade", 3.9)

    # To access the class method, utilize the class name and the access operator (`.`) followed by the class method name.
    # When the class method is called, we can access or modify class data
    print(Student.get_count())  # Print "Total number of students: 3"
    print(Student.get_avg_gpa())    # Print "Total average gpa: 0"

if __name__ == "__main__":
    main()