# Inheritance
# Allows a class to inherit attributes and methods from another class.
# Helps with readability and modularity
# The syntax for basic inherientance would be class Child(Parent)

from animal import Dog
from animal import Cat
from animal import Mouse

def name():
    pass

def main():
    dog = Dog("Butch")
    cat = Cat("Spots")
    mouse = Mouse("Hops")

    print(dog.name)
    print(dog.is_alive)
    dog.speak()
    dog.eat()
    dog.sleep()

    print(cat.name)
    print(cat.is_alive)
    cat.speak()
    cat.eat()
    cat.sleep()

    print(mouse.name)
    print(mouse.is_alive)
    mouse.speak()
    mouse.eat()
    mouse.sleep()

if __name__ == "__main__":
    main()