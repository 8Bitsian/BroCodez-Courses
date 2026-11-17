/*
    In C++, the `sizeof()` operator determines the size in bytes of a variable, data type, class, objetc, etc.

    To get the size of an array, use the `sizeof()` operator by pasing in a variable to get the size of a data type in bytes.
    Each of the primitive data types can be calcualted with a set amount of bytes:
    - For boolean values (i.e., `true` or `false`), they are 1 byte
    - For integer values (i.e., `int`), they are 4 bytes
    - For double values (i.e., `double`), they are 8 bytes
    - For character values (i.e., `char`), they are 1 byte
    - For string values (i.e., `string`), they are 32 bytes, regardless of how many characters are within the string

    To calculate the amount of bytes within an array, multiply the number of elements by the data type.
    The `sizeof()` operator can be used to find out how many elements an array has by dividing the size of the array by either:
    - The size of the first element in the array: `sizeof(array) / sizeof(array[0])`
    - The size of the array's data type: `sizeof(array) / sizeof(datatype)`
*/

#include <iostream>
using namespace std;

int main() {
    /// @brief The `main()` function is where the program begins
    /// @return 0 if the program terminated successfully, else a non-zero value if there was an issue

    // To get the size of an array, use the `sizeof()` operator by pasing in a variable to get the size of a data type in bytes.
    // For boolean values (i.e., `true` or `false`), they are 1 byte
    bool isStudent = true;
    cout << sizeof(isStudent) << " bytes" << endl;

    // For integer values (i.e., `int`), they are 4 bytes
    int courses = 4;
    cout << sizeof(courses) << " bytes" << endl;
    
    // For double values (i.e., `double`), they are 8 bytes
    double gpa = 2.5;
    cout << sizeof(gpa) << " bytes" << endl;

    // For character values (i.e., `char`), they are 1 byte
    char grade = 'B';
    cout << sizeof(grade) << " bytes" << endl;

    char grades[5] = {'A', 'B', 'C', 'D', 'F'};
    // To calculate the amount of bytes within an array, multiply the number of elements by the data type
    cout << sizeof(grades) << " bytes" << endl;
    // The `sizeof()` operator can be used to find out how many elements an array has by dividing the size of the array by either:
    // - The size of the first element in the array
    cout << (sizeof(grades) / sizeof(grades[0])) << " elements" << endl;
    // - The array's data type
    cout << (sizeof(grades) / sizeof(char)) << " elements" << endl;

    // For string values (i.e., `string`), they are 32 bytes, regardless of how many characters are within the string
    string name = "Imani Hollie";
    cout << sizeof(name) << " bytes" << endl;

    string college = "Gwinnett Technical College";
    cout << sizeof(college) << " bytes" << endl;

    return 0;
}