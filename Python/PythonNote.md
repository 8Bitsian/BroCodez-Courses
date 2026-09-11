# Python Note
A Python Note w/copy-and-paste templates for starting a multi-file Python project.

---
# Main File Setup

## File Header
Add this comment block at the top of each Python file when starting new files:
```python
# Project #: Name - Uses Notes #
# File: filename.py
# Description: Brief description of this file
# Uses: List of related files, classes, or modules
```

## Main method syntax for starting new main.py files:
@omp3policeo on Twitch for back-tick suggestion
```python
# Standard-library imports
import module_name
# Third-party or local library imports
from package_name import object_name

# Describe what this function does
def function_name():
    pass

# Runs the main program
def main():
    pass

if __name__ == "__main__":
    # print(f"Running {__name__}\n")
    main()
    # print("Program finished.")
```

---
# Module/Class File Setup

## Basic module syntax for starting new container.py files:
```python
# Project #: Project Name
# File: module_name.py
# Description: Brief description of this module

# Constant
CONSTANT_NAME = value

# Function
def function_name(parameter):
    pass
```

## Parent class syntax for defining inheritance between two classes/modules:
```python
# Project #: Project Name
# File: parent.py
# Description: Brief description of the parent class

class Parent:
    # Class Variables
    class_var = None

    # Constructor/Initialization Method
    def __init__(self, p_var):
        self.p_var = p_var

    # Instance Method
    def function(self):
        pass

    # Class Method
    @class_method
    def get_name(cls):
        return {cls.class_var}
```

## Child class syntax for defining inheritance between two classes/modules:
```python
# Project #: Project Name
# File: child.py
# Description: Brief description of the child class

from parent import Parent

class Child(Parent):
    # Constructor/Initialization Method
    def __init__(self, p_var, c_var):
        super().__init__(p_var)
        self.c_var = c_var

    # Override Inherited Method
    def function(self):
        pass

    # Getter Method
    @property
    def c_function(self):
        # Return the child variable
        return self.c_var

    # Setter Method
    @c_function.setter
    def c_function(self, new_var):
        # Update the child variable
        self.c_var = new_var

    # Deleter Method
    @c_function.deleter
    def c_function(self):
        # Delete the child variable
        del self.c_var
```
