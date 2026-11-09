/*
    Math related functions in C++ are part of the `<cmath>` library, which provides a variety of mathematical operations and constants.
    These functions can be used for tasks such as calculating square roots, trigonometric functions, logarithms, and more.

    If you head to www.cplusplus.com/references/cmath/ you can find a comprehensive list of all the functions available in the `<cmath>` library, along with their descriptions and usage examples.
*/

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    double x = 3.0;
    double y = 4.0;
    double z;

    // The max() and min() functions are standard functions in C++ that return the maximum and minimum of two values, respectively.
    // They are part of the `<algorithm>` header, but can also be used with `<cmath>` for basic types.

    // The max() function returns the larger of two values
    z = max(x, y);
    cout << "The maximum of " << x << " and " << y << " is " << z << endl;

    // The min() function returns the smaller of two values
    z = min(x, y);
    cout << "The minimum of " << x << " and " << y << " is " << z << endl;

    // The following functions are part of the `<cmath>` library and provide various mathematical operations:

    // The sqrt() function returns the square root of a value
    z = sqrt(x);
    cout << "The square root of " << x << " is " << z << endl;

    // The pow() function raises a value to the power of another value
    z = pow(x, y);
    cout << x << " raised to the power of " << y << " is " << z << endl;

    // The abs() function returns the absolute value of a number
    z = abs(-x);
    cout << "The absolute value of " << -x << " is " << z << endl;

    // The round() function rounds a floating-point number to the nearest integer
    z = round(3.6);
    cout << "The rounded value of 3.6 is " << z << endl;

    // The ceil() function rounds a floating-point number up to the nearest integer
    z = ceil(3.2);
    cout << "The ceiling value of 3.2 is " << z << endl;

    // The floor() function rounds a floating-point number down to the nearest integer
    z = floor(3.8);
    cout << "The floor value of 3.8 is " << z << endl;

    return 0;
}