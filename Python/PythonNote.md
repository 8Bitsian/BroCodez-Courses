# Python Note
Python Note for all of your copy + paste needs

# Comment syntax for starting new files:
```
# Project #: Name - Uses Notes #
# Detailed Description
```

# Main method syntax for starting new main.py files:
@omp3policeo on Twitch for backtick suggestion
```
import _
from _ import _

def name():
    pass

def main():
    pass

if __name__ == "__main__":
    # print(f"Called main.py file is: {__name__}\n")
    main()
    # print("Exiting main.py file...")
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