# Multiple Inheritances
# A Class can inherit traits (attributes and methods) from more than one parent class `C(A, B)`. Think like mother and father to child.

# Multi-level Inheritance
# A class can inherit from a parent which inherits from another parent `C(B) <- B(A) <- A`. Think like a grandfather to father to son.

import foodchain

def main():
    rabbit = foodchain.Rabbit("Skippy")
    hawk = foodchain.Hawk("Bullseye")
    fish = foodchain.Fish("Nemo")

    rabbit.flight() # Prints "<foodchain.Rabbit object at 0x00000266932716A0> is fleeing..."
    # rabbit.fight()  # Prints "AttributeError: 'Rabbit' object has no attribute 'fight'."
    rabbit.sleep()

    # hawk.flight() # Prints "AttributeError: 'Hawk' object has no attribute 'flight'"
    hawk.fight()  # Prints "<foodchain.Hawk object at 0x000002AFBDF617F0> is hunting..."
    hawk.eat()

    fish.flight() # Prints "<foodchain.Fish object at 0x0000023F0FB41940> is fleeing..."
    fish.fight()  # Prints "<foodchain.Fish object at 0x0000023F0FB41940> is hunting..."
    fish.eat()
    fish.sleep()

if __name__ == "__main__":
    # print(f"Called main.py file is: {__name__}\n")
    main()
    # print("Exiting main.py file...")