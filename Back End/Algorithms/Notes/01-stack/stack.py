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

    # The `size()` method uses the `len()` method
    def size(self):
        return len(self.stack)