/*
    In C++, the `typedef` keyword is used to create an additional name (alias) for an existing data type, allowing you to define a new name for a type that can be used interchangeably with the original type.
    This can be useful for improving code readability, simplifying complex type declarations, or creating more meaningful names for types in your program.

    `typedef` has been largely replaced by the `using` keyword in modern C++ (C++11 and later), which works better with templates. However, `typedef` is still widely used and supported in C++.
    The `using` keyword is a more modern and preferred way to create type aliases in C++. It provides better support for templates and is generally considered more readable.
*/

#include <iostream>
#include <vector>

using namespace std;

// typedef vector<pair<string, int>> pairList_t; // A common naming convention for `typedef` aliases is to use a descriptive name that ends with `_t`, indicating that it is a type alias.
// typedef string text_t; // You can also create a `typedef` alias for a simple data type like `string`, which can make the code more readable and easier to understand.
// typedef int number_t;

using pairList_t = vector<pair<string, int>>; // The `using` keyword is a more modern and preferred way to create type aliases in C++. It provides better support for templates and is generally considered more readable.
using text_t = string;
using number_t = int;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    pairList_t myPairList; // You can now use the alias `pairList_t` to declare variables of type `vector<pair<string, int>>`, making the code more concise and easier to read.
    text_t myText = "Hello, World!";
    number_t age = 23;

    cout << "My text is: " << myText << endl;
    cout << "My age is: " << age << endl;

    return 0;
}