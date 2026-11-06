/*
    C++ is used because it is a fast langauge and is commonly used in advanced graphics applications, embedded system, and video games.
    C++ is considered a middle level programming language: For context, Python, Java, and C# are considered high-level languages, or are closer to human language.

    There are two things you need to download to get started coding in C++:
        1. A Text Editor or an Integrated Development Environment (IDE)
            - You can use VSCodium, CodeBlocks, Notepad, etc. You can Go to [JetBrains.com](https://www.jetbrains.com/clion/) and download the latest version of the CLion IDE community version (it's free :3)
        2. A C/C++ Compiler
            - Go to [isocpp.org](https://isocpp.org/get-started) and download the latest version of [Clang](https://clangd.llvm.org/installation.html) or [GCC](https://gcc.gnu.org/install/). If you are using Windows, you can also download [MinGW](https://sourceforge.net/projects/mingw/).

    Comments aren't executed as code by the compiler and are used as notes for either yourself or other developers. There are a few types of comments:
        - A multiline (block) comment begins with a slash and an asterisk `/*` and can span multiple lines
        - A single line comment begins with two slashes `//` and spans a single line
*/

#include <iostream>     // `<iostream>` is a header file that contains basic functions for input/output operations

//using namespace std;  `std` means standard. The namespace `std` is where the C++ standard library is defined. You can use the `using` keyword to avoid having to type `std::` before every standard library function.

/// C++ doesn't have docstrings like higher level programming languages. Instead you can use a common format of documentation within block comments, or with a triple-slash `///` syntax, called Doxygen. */
/*
    You can use the `@brief` tag to provide a brief description of the function or class.
    You can use the `@param` tag to describe the parameters of the function.
    You can use the `@return` tag to describe the return value of the function.
*/

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    std::cout << "Hello, world. "; // `std::cout` is the standard output stream, and the left-shift operator `<<` is used to send data to the output stream. In this case, it sends the string "Hello, world. " to the console.
    
    // Every statement in C++ ends with a semicolon `;`. This is how the compiler knows that the statement is complete and can be executed. If you forget to include a semicolon, the compiler will throw an error.
    // The next line of code will print a string on the same line as the previous output. This is because there is no newline character `\n` or `std::endl` manipulator at the end of the previous statement.

    std::cout << "It is really sunny today!" << std::endl ; // The `std::endl` manipulator is used to insert a newline escape character `\n` and flush the output buffer.
    
    // This is useful when you want to ensure that all output is displayed immediately, especially in cases where the program may be waiting for user input or performing other tasks.
    
    std::cout << "I would like to go to the park." << "\n";      // You can also directly use the newline escape character `\n` to insert a new line in the output. It is similar to `std::endl`, but it does not flush the output buffer.
    std::cout << "Then, I think I'd like to go for icecream.\n"; // You can also use the backslash `\` to escape special characters in a string. In this case, it is used to escape the newline character `\n` so that it is treated as a literal character in the string.
    std::cout << "I would like two scoops of vanilla!";

    return 0;   // If the `main()` function returns 0, then the program terminated successfully, else if the function returns a non-zero value, then there was an issue.
}