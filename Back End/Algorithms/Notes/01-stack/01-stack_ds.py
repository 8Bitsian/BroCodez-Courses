# A stack is last-in first-out (LIFO) data structure that stores objects into a "vertical tower"
# The `push()` method adds to the top of the stack
# The `pop()` method removes from the bottom of the stack

from stack import Stack

# Your program implicitly starts here
def main():
    # Define a stack using arrays or linked lists
    myStack = Stack()

    # There are a few basic operations available for working with stacks
    print(f"Stack: {myStack.stack}\n")

    # The `isEmpty()` method checks if there are any elements in the stack
    print(f"isEmpty: {myStack.isEmpty()}\n")    # isEmpty = True

    # The `push()` method adds a new element on the top of the stack
    myStack.push('A')
    myStack.push('B')
    myStack.push('C')

    # You can use the `push()` and `pop()` methods with `for` loops
    # Be aware that you can overload the stack and cause a nerror with the heap
    for x in range(1, 3):
        myStack.push('D')

    print(f"Stack: {myStack.stack}\n")
    print(f"isEmpty: {myStack.isEmpty()}\n")    # isEmpty = False
    
    # The `pop()` method removes the top (last) element from the stack
    print(f"Pop: {myStack.pop()}\n")

    # The `size()`method checks how many elements are in the stack
    print(f"Size: {myStack.size()}\n")

    # The `peek()` method returns the top (last) element on the stack
    print(f"Peek: {myStack.peek()}\n")

if __name__ == "__main__":
    main()