/*
    In C++, an array is a data structure used to store multiple values in a single variable, which are then accessed via an index number.

    Arrays can be treated like variables that hold multiple values.
        After the variable name add square brackets `[]` and a set of curly braces `{}` around each value within the array
        You can use commas `,` to separate values in the list
        You can only add values of the same data type as the array
*/

#include <iostream>
using namespace std;

void carModels();
void lamboTwins();
void autobots();

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string car = "Corvette";
    cout << car << endl;

    carModels();
    lamboTwins();
    autobots();

    return 0;
}

void carModels() {
    /// @brief carModels() prints out array of different car models

    /*
        To declare an array, define the variable type (e.g., `int`, `double`, `string`, etc.), specify the name of the array followed by square brackets `[]`.
        To define an array, use an assignment operator `=` and an array literal using curly braces `{}` and insert a comma `,` separated list of values.
        You can only add values of the same data type as the array
    */
    string carModels[3] = { "Lamborghini", "Porsche", "Mustang" };

    /*
        Each value is stored in memory and can be accessed via an index.
        To access elements within an array, refer to the index number inside the square brackets `[]`, which always starts at 0.
    */
    cout << carModels[0] << endl;
    cout << carModels[1] << endl;
    cout << carModels[2] << endl;
}

void lamboTwins() {
    /// @brief lamboTwins() prints out array value after overriding by index

    string lamboTwins[1] = { "Sunstreaker" };
    cout << lamboTwins[0] << endl;

    // To change the value of a specific element, refer to the index number and use the assignment operator `=` and override previous values.
    lamboTwins[0] = "Sideswipe";

    cout << lamboTwins[0] << endl;
}

void autobots() {
    /// @brief autobots() prints out array of different autobots

    // You can declare an array and assign values later, so long as you specify the number of elements it should store within the square brackets `[]`.
    string autobots[3];

    autobots[0] = "Cliffjumper";
    autobots[1] = "Beachcomber";
    autobots[2] = "Cosmos";

    /*
        You can iterate through an array via a for loop to save line space

        Same as the following:
        cout << autobots[0] << endl;
        cout << autobots[1] << endl;
        cout << autobots[2] << endl;
    */

    for (int i = 0; i < 3; i++) { 
        cout << autobots[i] << endl;
    }
}