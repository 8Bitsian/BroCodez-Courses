/*
    In C++, a string is a sequence of characters that can be manipulated and stored in memory.
    The C++ Standard Library provides the `std::string` class, which is part of the `<string>` header, to handle strings more easily than using character arrays (C-style strings).
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    string name;

    cout << "Enter your name: ";
    getline(cin >> ws, name);
    // Use getline to read the entire line, including spaces
    // Includeing `ws` before `name` to consume any leading whitespace characters

    // The `length()` method will return the number of characters within a string
    cout << name.length() << endl;

    // The `empty()` method will return a boolean value depending on whether there are characters within a string
    (name.empty()) ? cout << "The string is empty." << endl : cout << "The string is full." << endl;

    // The `append()` method will insert a string within the parentheses to the end of another string
    name.append("@gmail.com");
    cout << name << endl;

    // The `at()` method will return the character at the specified index, starting with 0
    cout << name.at(0) << endl;

    // The `insert(pos, string)` method will insert a string at a speicied index within the 
    name.insert(0, "Your email is: ");
    cout << name << endl;

    // The `find()` method will return the first index of the specified character within a string
    cout << name.find(' ') << endl;

    // The `erase(start, end)` method will remove a portion of a string at a given index range
    name.erase(0, 15);
    cout << name << endl;

    // The `clear()` method will remove all characters within a string
    name.clear();
    (name.empty()) ? cout << "The string is empty." << endl : cout << "The string is full." << endl;

    return 0;
}