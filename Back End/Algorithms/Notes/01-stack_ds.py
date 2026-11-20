# A stack is last-in first-out (LIFO) data structure that stores objects into a "vertical tower"
# The `push()` method adds to the top of the stack
# The `pop()` method removes from the bottom of the stack

class Stack:
    def __init__(self):
        self.stack = []

    # The `push()` method uses the `append()` method
    def push(self, element):
        self.stack.append(element)

    # The `pop()` method removes and returns the top element from the stack
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    # The `peek()` method uses the `len()` method
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    # The `isEmpty()` method uses booleans values
    def isEmpty(self):
        return len(self.stack) == 0

    # the `size()` method uses the `len()` method
    def size(self):
        return len(self.stack)

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