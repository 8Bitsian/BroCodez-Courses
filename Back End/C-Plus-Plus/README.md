# Setup C++ File
C++ is used because it is a fast langauge and is commonly used in advanced graphics applications, embedded system, and video games.
It is considered a middle-level programming langauge: For context, Python, Java, and C# are considered high-level languages, or are closer to human language.

There are two things you need to download to get started coding in C++:
1. A Text Editor or an Integrated Development Environment (IDE)
- You can use VSCodium, CodeBlocks, Notepad, etc. You can Go to [JetBrains.com](https://www.jetbrains.com/clion/) and download the latest version of the CLion IDE community version (it's free :3)
2. A C/C++ Compiler
- Go to [isocpp.org](https://isocpp.org/get-started) and download the latest version of [Clang](https://clangd.llvm.org/installation.html) or [GCC](https://gcc.gnu.org/install/). If you are using Windows, you can also download [MinGW](https://sourceforge.net/projects/mingw/).

## Comments
Remember when setting up a C++ program to document what your program does as you develop a project.
It is good practice as when you eventually return to said program or for other developers to be able to understand what you are doing.

Comments aren't executed as code by the compiler and are used as notes for either yourself or other developers. There are a few types of comments:
- A multiline (block) comment begins with a slash and an asterisk `/*` and can span multiple lines
- A single line comment begins with two slashes `//` and spans a single line

C++ doesn't have docstrings like higher level programming languages. Instead you can use a common format of documentation within block comments, or with a triple-slash `///` syntax, called Doxygen.
- The `@brief` tag to provide a brief description of the function or class
- The `@param` tag to describe the parameters of the function
- The `@return` tag to describe the return value of the function

## First Program
When creating a C++ file, first we have to include the header file to import functions for us to be able to execute code.
The `#include <iostream>` line contains basic functions for input/output operations that allows us to write output, read input, and write a newline.

This isn't talked about in this section, but a `namespace` is a named scope that groups related names and helps prevent naming conflicts.
The C++ standard library `std` puts many of its names, including `cout`, `cin`, `string`, etc. inside the `std` namespace.
To use names within the `std` namespace without having to write `std::` each time utilize the `using` keyword: `using namespace std;`.

Every statement in C++ ends with a semicolon `;`. This is how the compiler knows that the statement is complete and can be executed. If you forget to include a semicolon, the compiler will throw an error.

When writing output to the console, we use the standard output stream `std::cout` and the left-shift operator `<<`.

The next line of code will print a string on the same line as the previous output.
This is because there is no newline character `\n` or `std::endl` manipulator at the end of the previous statement.

The end of line `std::endl` manipulator is used to insert a newline escape character `\n` and flush the output buffer.
This is useful when you want to ensure that all output is displayed immediately, especially in cases where the program may be waiting for user input or performing other tasks.

You can also use the backslash `\` to escape special characters in a string. In this case, it is used to escape the newline character `\n` so that it is treated as a literal character in the string.
You can also directly use the newline escape character `\n` after the left-shift operator to insert a new line in the output. It is similar to `std::endl`, but it does not flush the output buffer.

When ending a C++ funciton, we use the `return` keyword to end the current function and, if specified, send a value back to whoever called it.
In the `main()` funciton, `return 0;` ends the program and reports successful completion to the operating system. If the function returns a non-zero value, then there was an issue. 

```cpp title="01_setup.cpp"
// Header Files
#include <iostream>
//using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    std::cout << "Hello, world. ";
    std::cout << "It is really sunny today!" << std::endl ;
    std::cout << "I would like to go to the park." << "\n";
    std::cout << "Then, I think I'd like to go for icecream.\n";
    std::cout << "I would like two scoops of vanilla!";

    return 0;
}
```

# Variables and Basic Data Types

# `const`

# Namespaces

# `typedef`and Type Aliases

# Artithmetic Operators

# Type Conversion

# User Input

# Math Functions

# `if` statements

# Switches

# Ternary Operator

# Logical Operators

# `String` Methods

# `while` Loops

# `for` Loops

# `break` and `continue`

# Nested Loops

# `random`

# User Defined Functions

# `return` Keyword

# Overloaded Functions

# Variable Scope

# Arrays

# `sizeof()` Operator

# Iteration

# `foreach` Loop

# Pass Array to a Function

# Search array for an element

# Sort an array

# `fill()` Function

# Fill an array with User Input

# Multidimentional Arrays

# Memory addresses

# Pass by `value` vs. pass by `ref`

# `const` Parameters

# Pointes

# `null` pointers

# Dynamic Memory

# Recursion

# Function Templates

# `structs`

# Pass `structs` as arguments

# `enum`

# Object Oriented Programming

# Constructors

# Constructor Overloading

# Getters and Setters

# Inheritance
