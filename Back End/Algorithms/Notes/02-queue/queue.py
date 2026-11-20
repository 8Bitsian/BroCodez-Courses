class Queue:
    def __init__(self):
        self.queue = []

    # The `enqueue()` method uses the `append()` method
    def enqueue(self, element):
        self.queue.append(element)

    # The `dequeue()` method removes and returns the top element from the stack
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    # The `peek()` method uses the `len()` method
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    # The `isEmpty()` method uses booleans values
    def isEmpty(self):
        return len(self.queue) == 0

    # The `size()` method uses the `len()` method
    def size(self):
        return len(self.queue)

    # The `contains()` method uses the
    def contains(self, element):
        return element in self.queue