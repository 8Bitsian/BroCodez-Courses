/* 
    Arithmetic operators in C++ are used to perform mathematical operations on numeric values. The basic arithmetic operators include:
        - Addition (`+`): Adds two operands together.
        - Subtraction (`-`): Subtracts the right operand from the left operand.
        - Multiplication (`*`): Multiplies two operands together.
        - Division (`/`): Divides the left operand by the right operand.
        - Modulus (`%`): Returns the remainder of the division of the left operand by the right operand (only applicable to integer types).

    These operators can be used with variables, constants, and expressions to perform calculations in C++
*/

#include <iostream>

using namespace std;

using students_t = int;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    students_t numStudents = 25;

    cout << "Current number of students: " << numStudents << endl;

    /* 
        You can use arithmetic operators to perform calculations in two ways:
            1. Using the arithmetic operator directly in an expression: numStudents + 5
            2. Using the arithmetic operator in an assignment statement: numStudents = numStudents + 5;

        With the assignment statement, you are updating the value of `numStudents` by adding 5 to its current value and assigning the result back to `numStudents`.
        You can used the shorthand compound assignment operator `+=` to achieve the same result in a more concise way: numStudents += 5;
    */

    // The addition `+` operator is used to add two operands together.
    numStudents += 5; 
    cout << "After adding 5 students: " << numStudents << endl;

    // The increment/decrement operators are shorthand ways to increase or decrease the value of a variable by 1.
    // This operator can be used in two forms: prefix (`++numStudents`) and postfix (`numStudents++`).

    // Another way to increase the value of `numStudents` by 1 is to use the increment operator `++`.
    ++numStudents; // The prefix form increments the value of `numStudents` by 1 before it is used in an expression.
    cout << "After incrementing the number of students by 1: " << numStudents << endl;

    // The subtraction `-` operator is used to subtract the right operand from the left operand.
    numStudents -= 3;
    cout << "After removing 3 students: " << numStudents << endl;

    // Another way to decrease the value of `numStudents` by 1 is to use the decrement operator `--`.
    numStudents--; // The postfix form decrements the value of `numStudents` by 1 after it is used in an expression.
    cout << "After decrementing the number of students by 1: " << numStudents << endl;

    // The multiplication `*` operator is used to multiply two operands together.
    numStudents *= 2;
    cout << "After doubling the number of students: " << numStudents << endl;

    // The division `/` operator is used to divide the left operand by the right operand.
    numStudents /= 4;
    cout << "After dividing the number of students by 4: " << numStudents << endl;

    // The modulus `%` operator is used to find the remainder of the division of the left operand by the right operand.
    students_t remainder = numStudents %= 2; // The modulus operator `%` is only applicable to integer types. If you try to use it with floating-point types (like `float` or `double`), the compiler will throw an error.
    // The modulus operator can be useful in various scenarios, such as determining if a number is even or odd by checking if the remainder is 0 (even) or 1 (odd).
    cout << "After taking the remainder of the number of students divided by 2: " << remainder << endl;

    /*
        All arithmetic operators have an order of precedence, which determines the order in which operations are performed in an expression.
        The order of precedence for arithmetic operators is as follows (PEMDAS):
            1. Parentheses `()`
            2. Multiplication `*`, Division `/`, and Modulus `%` (from left to right)
            3. Addition `+` and Subtraction `-`
            4. Assignment `=`, Compound Assignment `+=`, `-=`, `*=`, `/=`, `%=` (from right to left)
            5. Increment `++` and Decrement `--` (from right to left)
            6. Negative `-` (unary minus) and Positive `+` (unary plus) (from right to left)

        You can use parentheses `()` to group operations and override the default order of precedence.
        Operations within parentheses are performed first, followed by multiplication, division, and modulus, and finally addition and subtraction
    */

    students_t result = 6 - (numStudents + 5) * 2 / 3;
    cout << "The result of 6 - (" << numStudents << " + 5) * 2 / 3 is: " << result << endl;

    return 0;
}