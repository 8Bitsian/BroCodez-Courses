# Magic (Dunder) Method
# Dunder methods (double underscore `__`) including `__init__`, `__str__`, `__eq__`, etc.
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects.

from classroom import Student
from library import Book

def main():
    student1 = Student("Wade", 3.9)
    student2 = Student("Mark", 3.4)

    print(student1)             # Print "Name: Wade GPA: 3.9"
    print(student1 == student2) # Print "False"
    print(student1 > student2)  # Print "True"

    # When creating objects we automatically call the dunder (magic) initialization method `__init__()`. This allows us to define the object by assigning attributes
    book1 = Book("The Sword in the Stone", "T. H. White", 312)
    book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    book3 = Book("American Gods", "Neil Gaiman", 465)

    # When we print object directly to the console we are given a memory address
    # Print "<library.Book object at 0x000001643CCBC830>"
    print(book1)   # Print "'The Sword in the Stone' by T. H. White"

    print(book1 == book1)
    print(book1 == book2)

    print(book2 < book3)
    print(book1 < book2)

    print(book2 < book3)
    print(book1 < book2)

    print(book1 + book3)

    print("Sword" in book1)
    print("Sword" in book2)
    print("Neil" in book3)
    print("Neil" in book2)

    print(book1["title"])
    print(book1["author"])
    print(book1["num_pages"])
    print(book1["audio"])

if __name__ == "__main__":
    main()