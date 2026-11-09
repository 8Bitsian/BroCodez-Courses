/*
    We can accept user input in C++ by manipulating the standard input/output streams using insertion operators.
    1. The `cin` object is used to read input from the standard input stream (keyboard) is paired with the extraction operator (`>>`) to extract data from the input stream and store it in variables
    2. The `cout` object is used to write output to the standard output stream (console) is paired with the insertion operator (`<<`) to insert data into the output stream for display
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string name;
    int age;

    cout << "Enter your age: ";
    cin >> age; // Read user input and store it in the variable 'age'

    cout << "Enter your name: ";
    getline(cin >> ws, name); // Read user input and store it in the variable 'name'
    // Note: Using `getline()` allows for reading full names with whitespaces, unlike `cin >> name` which stops at the first whitespace.
    // Include `ws` to consume any leading whitespace characters before reading the name, ensuring that the input is captured correctly.

    cout << "Hello, " << name << "!" << endl; // Output a greeting message with the user's name
    cout << "You are " << age << " years old." << endl; // Output the user's age

    return 0;
}