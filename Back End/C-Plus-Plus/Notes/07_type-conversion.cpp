/*
    Type conversion changes a value from one data type to another. It can happen:
        1. Implicitly, when the compiler performs a permitted conversion automatically.
        2. Explicitly, when the code requests a conversion with a cast.

    Converting a floating-point value to an integer truncates the fractional part
    toward zero. Use static_cast to make explicit conversions clear.
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    double original = 3.14;
    int implicitInt = original;
    double implicitDouble = 3;
    int explicitInt = static_cast<int>(original);
    double convertedBack = static_cast<double>(explicitInt);

    cout << "Implicit double-to-int: " << implicitInt << endl;
    cout << "Implicit int-to-double: " << implicitDouble << endl;
    cout << "Explicit double-to-int: " << explicitInt << endl;
    cout << "Converted back to double: " << convertedBack << endl;

    char letter = static_cast<char>(100);
    cout << "Character value: " << letter << endl;
    cout << "Numeric value of character: " << static_cast<int>(letter) << endl;
    cout << "Character for numeric value 101: " << static_cast<char>(101) << endl;

    return 0;
}