# Python Note

A Python Note w/copy-and-paste templates for starting a multi-file Python project.

---

# File Header
Add this comment block at the top of each Python file when starting new files:

```python
# Project #: Name - Uses Notes #
# File: filename.py
# Description: Brief description of this file
# Uses: List of related files, classes, or modules
```

# Main method syntax for starting new main.py files:
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

# Class syntax for starting new class.py files:
```
class Parent:
    # Class Variables
    class_var

    # Constructor/Initialization Method
    def __init__(self, p_var):
        self.p_var = p_var

    # Instance Method
    def function(self):
        pass

    # Class Method
    @classmethod
    def get_name(cls):
        return {cls.class_var}"

class Child(Parent):
    # Constructor/Initialization Method
    def __init__(self, p_var, c_var):
        super().__init__(p_var)
        self.c_var = c_var
        
    # Functions
    def function(self):
        pass

    # Getter Method
    @property
    def c_function(self):
        return {self.c_var}

    # Setter Method
    @c_function.setter
    def c_function(self, new_var):
        self.c_var = new_var

    # Deleter Method
    @c_function.deleter
    def c_function(self):
        del self.c_var
```
