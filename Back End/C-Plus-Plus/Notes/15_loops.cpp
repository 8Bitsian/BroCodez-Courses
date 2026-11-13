/*
    This note is a combination of `while`, `do while`, `for`, and `for each` loops.
    It also covers the `break` and `continue` keywords as well as nested loops.

    A `while` loop is similar to an `if` statement, except we are able to execute code a near infinite amount of times.
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    /*
        In C++, `while` loops are similar to `if` staements, in that they check if a condition is `true` or `false`, and differ in that they use that check to determine whether to repeat, or iterate, the statements within the code block between thier curly braces.

        `if` `name` is empty then print "The string is empty." `else` print "The string is full."
        (name.empty()) ? cout << "The string is empty." << endl : cout << "The string is full." << endl;

        A `while` loop will repeat until the condition within the parentheses is valid or `true`
        A loop with no way out is considered an infinite loop.

        The syntax is: while (condition) { ... }
    */

    string name;
    while (name.empty()) {
        cout << "Enter your name: ";
        getline(cin >> ws, name);
    }
    cout << "Hello " << name << endl;

    /*
        In C++, a `do-while` loop executes a block of code after `do` and iterates if a condition is valid or `true`
        The syntax is: do { ... } while (condition)
    */

    int value = 0, number;
    do {
        cout << "Enter a value: ";
        cin >> number;
        value += number;
    } while (value < 10);
    cout << "Sum: " << value << endl;

    /*
        In C++, a `for` loop executes a block of code a specified amount of times.

        Within the condition for the for loop there are three parts we can include:
            1. The index which acts as a counter for the amount of times the code block executes
            2. The limit which acts as a stopping point for the loop
            3. Then the increment/decrement for the counter to add or subtract by the amount of loops

        You can set the index to be anything greather than or equal to 0.

        When incrementing/decrementing you are able to skip iterations by using values more than 1.
        
        The syntax is: for (index; limit; increment/decrement ) { ... }
    */

    for (int i = 1; i <= 10; i++) {
        cout << "Countdown: " << i << endl;
    }
    cout << "Happy New Year!" << endl;

    /*
        In C++, a `for each` loop eases the traversal over an iterable data set, such as an array.

        Using a `for` loop, you must include three statements, an index, a condition, and then increment/decrement the index.
        The `for` loop allows you to increment/decrement, or skip iterations.
        
        The `for each` loop is simpler than a for loop, but it is less flexible syntax wise.
        It only allows us to start at the beginning index and increment forward towards the ending index.
    */

    string autobots[] = {"Ironhide", "Sunstreaker", "Jazz", "Prowl"};
    for (int i = 0; i < sizeof(autobots) / sizeof(autobots[0]); i++) {
        cout << "Rollcall: " << autobots[i] << endl;
    }
    cout << "Transform and Roll Out!" << endl;

    string decepticons[] = {"Breakdown", "Knockout", "Starscream", "Soundwave"};
    // The syntax is: for (element in dataset) { ... }
    for (string con : decepticons) {
        cout << "Rollcall: " << con << endl;
    }
    cout << "Transform and Rise Up!" << endl;

    /*
        In C++, the `break` keyword will step out of a loop (also seen in `switch` statements), while the `continue` keyword will skip a current iteration.
    */

    for (int i = 1; i <= 10; i++) {
        if (i == 3) {
            continue;  // The outer `for` loop will skip the 3rd iteration and will not print and then continue
        } else if (i == 7) {
            break;  // The outer `for` loop is broken at the 7th iteration and will not continue to 10
        }
        // We don't have to put an else statement as it's implied
        cout << i << endl;
    }
    cout << "The for loop is over." << endl;

    /*
        In C++, nexted loops are loops within loops.
        The outer most loop dictates how many iterations there are for the inner most loop
        A common naming convention for nested loops is to use `i` as the outer most index and `j` as the inner most index

        loop (i = value) {
            ( ... ) // Iterates i times
            loop (j = value) {
                ( ... ) // Iterates i * j times
            }
            cout << "Exiting inner most for loop." << endl;
        }
        cout << "Exiting outer most for loop." << endl;


    */

    int row, col;
    char symbol = '-';

    cout << "How many rows? ";
    cin >> row;

    cout << "How many columns? ";
    cin >> col;

    cout << "Enter a symbol to print: ";
    cin >> symbol;

    // A common naming convention for nested loops is to use `i` as the outer most index and `j` as the inner most index
    for (int i = 1; i <= row; i++) {
        for (int j = 1; j <= col; j++) {
            cout << symbol;
        }
        cout << endl;
    }

    return 0;
}