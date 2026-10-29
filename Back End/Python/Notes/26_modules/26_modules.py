# Modules
# Modules are python files containing code you want to include in your program by using the `import` keyword to include within a program (built-in or custom-made)
# Modules are useful to break up a large program into reusable separate files.

# For a list of all of the modules within the standard python library use the help() method and pass in the word "modules" `print(help("modules"))`

# You are able to give imported module names aliases with the `as` keyword
import math as m

# Instead of importing the entire module, you can specify which methods you would like to access with the `from` keyword
# This method isn't used as much because of possible of variable naming conflictions
# from math import e

# You would then refer to that module by it's alias
print(m.pi) # Prints "3.141592653589793"
print(m.e)    # Prints "2.718281828459045"

# You can import custom-made modules via referencing their file names so long as they are within the same project folder
# File names for method must not contain underscores or start with numbers
import mathmethod as mm
result = mm.pi
print(result)
result = mm.square(3)
print(result)
result = mm.cube(3)
print(result)
result = mm.circumference(3)
print(result)
result = mm.area_circle(3)
print(result)