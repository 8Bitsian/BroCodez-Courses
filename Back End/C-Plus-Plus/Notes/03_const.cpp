/*
    The `const` keyword in C++ is used to declare variables whose values cannot be changed after initialization because they are constant.
    This means that once a `const` variable is assigned a value, it cannot be modified throughout the program (variable is then considered read-only).
    Using `const` can help prevent accidental changes to variables that should remain constant, improving code safety and readability.
*/

// Standard-library includes
# include <iostream>

using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    const double PI = 3.14159; // A popular naming convention for `const` variables is to use all uppercase letters with underscores to separate words.
    double radius = 5.0; // The `radius` variable is declared as a regular (non-const) variable, which means its value can be changed later in the program if needed.

    double circumference = 2 * PI * radius;

    cout << "The circumference of a circle with radius " << radius << " is: " << circumference << endl;

    const int LIGHT_SPEED = 299792458; // The speed of light in meters per second is a constant value that does not change, so it is declared as a `const` variable.

    const int WIDTH = 1920; // The width of a standard Full HD display is a constant value that does not change, so it is declared as a `const` variable.
    const int HEIGHT = 1080; // The height of a standard Full HD display is a constant value that does not change, so it is declared as a `const` variable.

    return 0;
}