/*
    In C++, scope detemines where a variable name can be used in a program.

    Variables are only accessible inside the region they are created within, i.e., scope:
        - Global scope is declared outside all functions
        - Local (block) scope is declared inside a function body and is visible only within that block `{}`

    A variable declared in an inner scope can have the same name as one in an outer scope, but not vice versa.
    The inner variable then hides (shadows) the outer one with the inner scope.
    C++ will treat them as separate variables.

     Global-scope variable are available anywhere within the program, unless a local vairable with the same name shadows it.
    `::` can be used to delibrately access the global or outer scope variables.
*/

#include <iostream>
using namespace std;

// Global-scope variable are available anywhere within the program, unless a local vairable with the same name shadows it.
int NUMBER = 67;

void myFunction() {
    cout << NUMBER << endl; // Refers to global variable

    int varNum = 23;
    cout << varNum << endl; // Refers to local myFunc variable
}

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int NUMBER = 45;            // Local to main; Hides the global variable in main
    cout << NUMBER << endl;     // Refers to local main variable

    int varNum = 19;            // Local to main
    cout << varNum << endl;     // Refers to local main variable

    myFunction();               // Local variables are distinct from main's

    cout << ::NUMBER << endl;   // Accesses the global variable

    return 0;
}