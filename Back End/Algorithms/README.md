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

# Stack Data Structures
A stack is last-in first-out (LIFO) data structure that stores objects into a "vertical tower"

The following are basic operations used to manipulate data within the stack:
- The `push()` method adds to the top of the stack
- The `pop()` method removes from the bottom of the stack
- The `peek()` method returns the top (last) element on the stack
- The `isEmpty()` method checks if there are any elements in the stack
- The `size()`method checks how many elements are in the stack

## Example
```python title="01-stack_ds.py"
def main():
    # Push
    stack.append(1)
    stack.append(2)
    stack.append(3)

    # Peek
    topElement = stack[-1]
    print(f"Peek: {topElement}")

    # Pop
    poppedElement = stack.pop()
    print(f"Pop: {poppedElement}")

    # Is Empty?
    isEmpty = not bool(stack)
    print(f"isEmpty: {isEmpty}")

    # Size?
    print(f"Size: {len(stack)}")

if __name__ == "__main__":
    main()
```

# Notes

## Example
```python title="01-stack_ds.py"
def function_name():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
```