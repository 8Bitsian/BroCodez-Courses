# Multithreading
# Mutlithreading is used to perform multiple tasks concurrently (i.e., multitasking).
# It's good for input/output (I/O) bound tasks like reading files or fetching data from APIs threading (Ex. `Thread(target=my_function)`).

import threading    # Allows use of the threading constructor
import time

class Kid:
    # Constructor/Initialization Method
    def __init__(self, kid):
        self.kid = kid

    # Instance Method
    def whose_turn(self):
        print(f"It is {self.kid}'s turn for chores!")

class Chores(Kid):
    # Constructor/Initialization Method
    def __init__(self, kid, chore):
        super().__init__(kid)
        self.chore = chore

    # Override Inherited Method
    def whose_turn(self):
        super().whose_turn()

        match self.chore:
            case 1:
                self.walk_dog()
            case 2:
                self.take_out_trash()
            case 3:
                self.wash_dishes()
            case 4:
                self.do_laundry()
            case 5:
                self.get_mail()
            case _:
                print(f"{self.kid} has no more chores left! ✨")

    # Functions
    def walk_dog(self, f_name, l_name):
        time.sleep(5)
        print(f"{self.kid} finished walking {f_name} {l_name}. 🐶")

    def take_out_trash(self):
        time.sleep(4)
        print(f"{self.kid} finished throwing out the trash. 🗑️")

    def wash_dishes(self):
        time.sleep(3)
        print(f"{self.kid} finished washing the dishes. 🍽️")

    def do_laundry(self):
        time.sleep(2)
        print(f"{self.kid} finished putting away your clothes. 👕")

    def get_mail(self):
        time.sleep(1)
        print(f"{self.kid} finshed getting the mail. 📮")

    # Getter Method
    @property
    def which_chore(self):
        return self.chore

    # Setter Method
    @which_chore.setter
    def which_chore(self, new_chore):
        self.chore = new_chore