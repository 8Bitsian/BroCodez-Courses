# Magic (Dunder) Method
# Dunder methods (double underscore `__`) including `__init__`, `__str__`, `__eq__`, etc.
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects.

class Book:
    # Constructor/Initialization Method
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # String Method
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Is Equal to Method
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # Is Less Than Method
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    # Is Greater Than Method
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # Add Method
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    # Contains Method
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # Get Item Method
    def __getitem__(self, key):
        if (key == "title"):
            return self.title
        elif (key == "author"):
            return self.author
        elif (key == "num_pages"):
            return self.num_pages
        else:
            return f"key '{key}' was not found..."