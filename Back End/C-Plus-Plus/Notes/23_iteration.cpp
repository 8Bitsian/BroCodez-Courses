#include <iostream>
using namespace std;

void noLoop(string autobots[5]) {
    /// @brief Iterate over the autobots[] array and print elements w/a for loop
    /// @param autobots[5] array contains 5 cybertronians

    cout << "Print elements of array manually: " << endl;
    cout << autobots[0] << endl;
    cout << autobots[0] << endl;
    cout << autobots[0] << endl;
    cout << autobots[0] << endl;
    cout << autobots[0] << endl << endl;
}

void forLoop(string autobots[5]) {
    /// @brief Iterate over the autobots[] array and print elements w/a for loop
    /// @param autobots[5] array contains 5 cybertronians

    cout << "Print elements of array w/for loop: " << endl;

    // Set the index to 0 since the first array has an index of 0
    // Iterate by using the number of elements using the sizeof() operator
    for (int i = 0; i < (sizeof(autobots) / sizeof(string)); ++i) {
        cout << autobots[i] << endl;
    }
    cout << endl;
}

void forEachLoop(string autobots[5]) {
    /// @brief Iterate over the autobots[] array and print elements w/a for each loop
    /// @param autobots[5] array contains 5 cybertronians

    cout << "Print elements of array w/for each loop: " << endl;

    // Use an index for each element of the array
    // A common naming convention is to use 
    for (string autobot : autobots) {
        cout << autobots[autobot] << endl;
    }
    cout << endl;
}

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string autobots[5] = { "Ratchet", "Ironhide", "Bumblebee", "Grimlock", "Sludge" };

    noLoop(autobots);
    forLoop(autobots);
    forEachLoop(autobots);
    
    return 0;
}