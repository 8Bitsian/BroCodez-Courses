# A queue is first-in first-out (FIFO) data structure that stores objects into a "horizontal line"
# The `enqueue()` method adds to the back of the queue
# The `dequeue()` method removes from the front of the queue

from queue import Queue

# Your program implicitly starts here
def main():
    # Define a queue using arrays or linked lists
    myQueue = Queue()

    # There are a few basic operations available for working with queues
    print(f"Queue: {myQueue.queue}\n")

    # The `isEmpty()` method checks if there are any elements in the queue
    print(f"isEmpty: {myQueue.isEmpty()}\n")    # isEmpty = True

    # The `enqueue()` method adds a new element on the top of the queue
    myQueue.enqueue("Tems")
    myQueue.enqueue("Lauryn Hill")
    myQueue.enqueue("SZA")

    # You can use the `enqueue()` and `dequeue()` methods with `for` loops
    # Be aware that you can overload the queue and cause an error with the heap
    for x in range(1, 3):
        myQueue.enqueue("Tyla")

    print(f"Queue: {myQueue.queue}\n")
    print(f"isEmpty: {myQueue.isEmpty()}\n")    # isEmpty = False
    
    # The `dequeue()` method removes the top (last) element from the queue
    print(f"Pop: {myQueue.dequeue()}\n")

    # The `size()`method checks how many elements are in the queue
    print(f"Size: {myQueue.size()}\n")

    # The `peek()` method returns the top (last) element in the queue
    print(f"Peek: {myQueue.peek()}\n")

    # The `contains()` method returns a booleans for if there is a matching element within the queue
    print(f"Contains \"Tems\": {contains(myQueue, "Tems")}")    # Prints "Contains "Tems": True"
    print(f"Contains \"SZA\": {contains(myQueue, "SZA")}")    # Prints "Contains "SZA": False"

if __name__ == "__main__":
    main()