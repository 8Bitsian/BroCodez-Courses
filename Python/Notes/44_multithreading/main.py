# Multithreading
# Mutlithreading is used to perform multiple tasks concurrently (i.e., multitasking).
# It's good for input/output (I/O) bound tasks like reading files or fetching data from APIs threading (Ex. `Thread(target=my_function)`).

# To use the threading constructor, import the `threading` module
import threading
import chores

def main():
    good_kid = chores.Chores(kid="Steven", chore=3)
    print(good_kid) # Prints "<chores.Chores object at 0x000002C3505AC150>"
    # good_kid.whose_turn()   # Prints "It is Steven's turn for chores!
    #                         #         Steven finished washing the dishes. 🍽️"

    # good_kid.which_chore = 5
    # print(good_kid.which_chore) # Prints "5"

    # good_kid.whose_turn()   # Prints "It is Steven's turn for chores!
    #                         #         Steven finshed getting the mail. 📮"

    # good_kid.which_chore = 0
    # good_kid.whose_turn()   # Prints "It is Steven's turn for chores!
    #                         #         Steven has no more chores left! ✨"

    # The `threading` module creates a `Thread()` objects and tells it which target function to run later. It passes the method `"target=object.function"` as the target and only runs when you call the `start()` method.

    chore1 = threading.Thread(target=good_kid.walk_dog, args=("Scooby", "Doo"))
    chore2 = threading.Thread(target=good_kid.take_out_trash)
    chore3 = threading.Thread(target=good_kid.wash_dishes)
    chore4 = threading.Thread(target=good_kid.do_laundry)
    chore5 = threading.Thread(target=good_kid.get_mail)

    # The `start()` and `join()` methods control the execution of a Python thread.

    # The `.start()` method begins running the thread's target function in a separate thread so the main program can continue runnign while the task executes
    chore1.start()
    chore2.start()
    chore3.start()
    chore4.start()
    chore5.start()

    # The `.join()` method makes the current thread wait to print the next line in the console until another thread finishes
    chore1.join()
    chore2.join()
    chore3.join()
    chore4.join()
    chore5.join()

    print("\nAll chores are complete! ✨")

if __name__ == "__main__":
    main()