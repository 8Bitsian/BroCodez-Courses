# Data Structures and Algorithms
This directory will cover the following topics:
1. Basic data structures
2. Big O notation
3. Searching algorithms
4. Sorting algorithms
5. Graphs
6. Trees

A data structure is a named location that can be used to store and organize data.

Examples of data structures include:
- Trees, which are a hierarchy of family relationships
- Arrays, which is a collection of elements stored at contigous memory locations

An algorithm is a collection of steps to solve a problem.

Examples of algorithms include:
- Linear search, which parses a data structure one element at a time

Why would you need to know about data structures or algorithms?
1. You'll write code that is both time and memory efficient
2. Commonly asked questions involve DS&A in coding and job interviews

# Stacks
A stack is last-in first-out (LIFO) data structure that stores objects "vertically."
Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.

Stacks can be implemented using arrays or [linked lists](#linked-lists), which we will cover later on.
They are often mentioned with [Queues](#Queues), which is a similar data structure covered in the next section.

The following are basic operations used to manipulate data within a stack:
- The `push()` method adds to the top of the stack
- The `pop()` method removes from the bottom of the stack
- The `peek()` method returns the top (last) element on the stack
- The `isEmpty()` method checks if there are any elements in the stack
- The `size()` method checks how many elements are in the stack

## Example
```python title="01-stack_ds.py"
def main():
    stack = []

    # Is Empty?
    isEmpty = not bool(stack)
    print(f"isEmpty: {isEmpty}")    # Prints "isEmpty: True"

    # Push
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(f"Stack: {stack}")        # Prints "Stack: [1, 2, 3]"

    # Is Empty?
    isEmpty = not bool(stack)
    print(f"isEmpty: {isEmpty}")    # Prints "isEmpty: False"

    # Peek
    topElement = stack[-1]
    print(f"Peek: {topElement}")    # Prints "Peek: 3"

    # Pop
    poppedElement = stack.pop()
    print(f"Pop: {poppedElement}")  # Prints "Pop: 3"

    # Size?
    print(f"Size: {len(stack)}")    # Prints "Size: 2"

if __name__ == "__main__":
    main()
```

# Queues
A queue is a first-in first-out (FIFO) data structure that stores objects "horizontally."
It is a collection designed for holding elements prior to processing and is considered a linear data structure.
Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

Queues can be implemented using arrays or [linked lists](#linked-lists).

The following a basic operations used to manipulate data within a queue:
- The `enqueue()` method (similar to the `push()` method) adds to the back of the queue
- The `remove()` method (similar to the `pop()` method) removes to the front of the queue

Queues also uses the `peek()`, `isEmpty()`, and `size()` methods to parse through the elements.

## Example
```python title="02-queue_ds.py"
from collections import deque

def main():
    def contains(queue, element):
        return element in queue
    
    queue = deque()

    # Is Empty?
    print(f"isEmpty: {not queue}")  # Prints "isEmpty: True"

    # Enqueue (like `push()`)
    queue.extend(['A', 'B', 'C'])
    print(f"Queue: {list(queue)}")  # Prints "Queue: ['A', 'B', 'C']"

    # Is Empty?
    print(f"isEmpty: {not queue}")  # Prints "isEmpty: False"

    # Peek
    print(f"Peek: {queue[0]}")      # Prints "Peek: A"

    # Dequeue (like `pop()`)
    dequeued = queue.popleft()
    print(f"Dequeue: {dequeued}")  # Prints "Dequeue: A"

    # Size?
    print(f"Size: {len(queue)}")    # Prints "Size: 2"

    # Is Match?
    print(f"Contains \"C\": {contains(queue, 'C')}")    # Prints "Contains "C": True"
    print(f"Contains \"A\": {contains(queue, 'A')}")    # Prints "Contains "A": False"

if __name__ == "__main__":
    main()
```

## Priority Queues

### Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Linked Lists

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Dynamic Arrays

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Big O Notation

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Linear Search

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Binary Search

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Interpolation Search

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Bubble Sort

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Selection Sort

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Insertion Sort

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Recursion

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Merge Sort

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Quick Sort

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Hash Tables

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Linear Graphs

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Adjacency Matrix

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Adjacency Lists

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Depth First Search

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Breadth First Search

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Trees

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Binary Search Trees

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Tree Traversal

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```

# Calculate Execution Time

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```