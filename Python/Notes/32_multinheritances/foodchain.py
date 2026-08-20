# Animal is the "grandparent" class, so everything inherits it
class Animal:
    # Put the construtor in the main parent (orin this case grandparent) class
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")
    
    def sleep(self):
        print(f"{self.name} is asleep...")

# Prey and Predator inherits from the Animal class
class Prey(Animal):
    def flight(self):
        print(f"{self.name} is fleeing...")

class Predator(Animal):
    def fight(self):
        print(f"{self.name} is hunting...")

# Rabbit, Hawk, and Fish inherits from the Prey and Predator class
class Rabbit(Prey):
    # Rabbits will inherit the prey class
    pass

class Hawk(Predator):
    # Hawks will inherit the predator class
    pass

# To inherit from multiple parent classes, add them to the inheritance list
class Fish(Prey, Predator):
    # Fish will inherit both parent classes via multiple inheritances
    pass