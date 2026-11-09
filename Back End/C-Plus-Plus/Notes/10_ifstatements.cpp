/*
    C++ has decision structures to decide which statements to execute based on certain conditions.
    The `if` statement is used to execute a block of code if a specified condition is true. If the condition is false, the block of code is skipped.
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    int age;

    cout << "Please enter your age: ";
    cin >> age;

    /*
        The `if` statement is used to execute a block of code if a specified condition is either true or false. If the condition is false, the block of code is skipped.
        The `else if` statement is used to specify a new condition to test, if the previous condition was false. If the new condition is true, the block of code inside the `else if` statement will be executed.
        The `else` statement is used to execute a block of code if the condition(s) in the `if` and `else if` statements are false. If the condition is true, the block of code inside the `else` statement will be skipped.
        
        The `if` statement uses conditional operators to compare values within the parentheses `()`.

        The condition is evaluated to either true or false. A few condition operators are:
            1. `==` (equal to)
            2. `!=` (not equal to)
            3. `>` (greater than)
            4. `<` (less than)
            5. `>=` (greater than or equal to)
            6. `<=` (less than or equal to)
    */

    if (age >= 120) { // If the condition is true, the block of code inside the curly braces `{}` will be executed.
        cout << "Entered invalid age." << endl;
    } else if (age >= 21) { // If the condition is false, the block of code will be skipped and the code inside the `else if` block will be executed instead.
        cout << "You are an adult." << endl;
    } else if (age >= 0) {
        cout << "You are a minor." << endl;
    } else { // If every condition is false, the code inside the `else` block will be executed instead.
        cout << "Invalid age." << endl;
    }

    return 0;
}