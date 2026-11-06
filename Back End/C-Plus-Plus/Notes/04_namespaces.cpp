/*
    The `namespace` keyword in C++ is used to group related variables, functions, and classes under a single name to avoid naming conflicts in larger programs.
    Namespaces help organize code and prevent collisions between identifiers that may have the same name but are used in different contexts.
*/

// Standard-library includes
# include <iostream>

using namespace std; // The `using` keyword allows you to use names from a namespace without having to prefix them with the namespace name. In this case, it allows you to use `cout` and `endl` without the `std::` prefix.

namespace first {
    int x = 1; // You can declare similarly named variables, functions, and classes within a namespace.
}

namespace second {
    int x = 2;
}

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int x = 0;  // This variable `x` is declared in the global namespace, which means it is accessible throughout the entire program unless shadowed by a local variable with the same name.

    cout << "Global namespace x is: " << x << endl;
    cout << "\"first\" namespace is: " << first::x << endl; // To access a variable, function, or class within a namespace, you can use the scope resolution operator `::` followed by the namespace name and the identifier name.
    cout << "\"second\" namespace is: " << second::x << endl;

    return 0;
}