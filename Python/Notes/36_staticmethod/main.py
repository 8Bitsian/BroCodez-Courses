# Static Methods
# Methods that belong to individual objects from classes are instance methods.
# Instance methods are best for operations on instances of the class (objects).
# EX. def get_info(self): return f"{self.name} = {self.position}"

# Static methods belong to a class rather than any object from that class (instance). Usually used for general utility functions.
# Static methods are best used for utility functiuons that do not need access to class data.
# EX. @staticmethod def km_to_mi(kilometers): return kilometers * 0.621371

from employee import Employee

def main():
    # To call a static method, use the class name and the access operator (`.`)
    print(Employee.is_valid_pos("Cook"))            # Print "False"
    print(f"{Employee.is_valid_pos("Administrator")}\n")   # Print "True"

    # The following assignment creates an Employee object
    employee1 = Employee("Steven", "IT Specialist")
    employee2 = Employee("Marigold", "Administrator")
    employee3 = Employee("Philip", "Developer")
    employee4 = Employee("Cherry", "Engineer")

    # To call an instance method for an object, repeat the same syntax
    print(employee1.get_info()) # Print "Steven = IT Specialist"
    print(employee2.get_info()) # Print "Marigold = Administrator"
    print(employee3.get_info()) # Print "Philip = Developer"
    print(employee4.get_info()) # Print "Cherry = Engineer"

if __name__ == "__main__":
    main()