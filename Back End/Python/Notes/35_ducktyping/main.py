# Duck Typing
# Another way to achieve polymorphism besides inheritance
# Object can be treated as a different type of object but must have the minimum necessary attributes/methods
# "If it looks like a duck, walks like a duck, and quacks like a duck, it must be a duck"

import animals

def main():
    dog = animals.Dog()
    cat = animals.Cat()
    car = animals.Car()

    mammals = [dog, cat, car]
    for mammal in mammals:
        mammal.speak()
        print(f"{mammal.alive}\n")

if __name__ == "__main__":
    main()