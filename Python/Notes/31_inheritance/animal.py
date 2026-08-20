# Inheritance
# Allows a class to inherit attributes and methods from another class.
# Helps with readability and modularity
# The syntax for basic inherientance would be class Child(Parent)

# The parent class is the most broad
class Animal:
    # Class Variables

    # Constructor/Initialization Method
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    # Functions
    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is asleep...\n")

# The following child classes are more specific and inherient traits (attributes and methods) from the parent class
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")