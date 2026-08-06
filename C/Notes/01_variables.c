// To begin programming in C, you have to include the following header files:
#include <studio.h>   // Means "Standard I/O (input output)"
#include <stdbool.h>  // Means "Standard Boolean"

int main() {
  /*
    Single line comments use two back-slashes (//)
    Multi-line (block) comments use the backslash and the asterisk (/*) to enclose the comment over multiple lines
  
    Variable - A reusable contianer for a value. Behaves as if it were the value it contains. 
    
    There are four different data types [@BroCodez](https://www.youtube.com/watch?v=ix9cRaBkVe0) will discuss:
    1. Integer (int): A whole number
    2. Floats (float): A floating-point number (w/6-7 decimal places)
    3. Double (double): A floating-point number (w/15-16 decimal places)
    4. Character (char): A singular alphanmeric character
    5. String (char w/array): A string is just a char data type array that stores more than one alphanumeric character
    6. Boolean (bool): Holds two an expression or states - True or False
  */

  
  // Variables can be assigned values via the assignment operator (=)
  // Each statement must be ended w/a semicolon (;) 
  int age = 23;

  // To display variables, we use the printf statement (printf()) and a format specifier
  // In this case, to display an integer the format specifier is "%d"
  printf("You are %d years old. ", age); // Prints "You are 23 years old. "

  // If you add a decimal portion to an integer variable, the value after the decimal is truncated
  int year = 2025.5;
  printf("The year is %d.\n", year); // Prints "You are 23 years old. The year is 2025."
  
  // The previous two print statements printed onto the same line.
  // To access the next line in the console, be sure to end your string with a new line escape character
  int quantity = 5;
  printf("You have ordered %dx item(s).\n", quantity); // Print "You have ordered 5x item(s)."

  // To store a decimal portion, we need to use the float data type.
  float gpa = 3.2;
  // To display a float the format specifier is "%f"
  printf("Your gpa is %f\n", gpa);  // Prints "Your gpa is 3.200000"
  
  // C will automatically print 6-7 digits for floats so you need to include the rounding specifier to limit the number of decimal spaces
  // Will be dicussed in more detail in a later video
  printf("Your gpa is %.1f\n", gpa);  // Prints "Your gpa is 3.2"
  
  float price = 19.99;
  printf("The price is $%.2f\n", price); // Prints "The price is $19.99"

  float temp = -10.1;
  // To add the degree symbol on Windows type: [Alt] + 0176
  printf("The temperature is %.2f°C\n", temp); // Prints "The temperature is -10.10°C"

  // For more precision, we can use another datatype known as a double which can store up to 15-16 decimal places
  double pi = 3.14159265358979;
  // To display a double the format specifier is %lf meaning "long float", which is essentialy what a double actually is
  // The defualt behavior of C will print only 6 digits after the decimal, so this prints "The value of pi is 3.14592"
  printf("The value of pi is %.lf\n", pi);
  // To print the entire value, you'll have to include the rounding specifier to increase the number of deicimal spaces
  printf("The value of pi is %.15lf\n", pi); // Prints "The value of pi is 3.14159265358979"

  double e = 2.7182818284590;
  printf("The value of Euler's number (e) is %.15lf\n", e); // Prints "The value of Euler's number (e) is 2.7182818284590"

  // To store singular characters, we use the char data type.
  // When assigning a value to a char data type use single quotes ('')
  char grade = 'A';
  // To display a char the format specifier is %c
  printf("Your grade is %c", grade);  // Prints "Your grade is A"

  // You can also display various symbols using the char data type
  char symbol = '@';
  printf("Your symbol is %c\n", symbol);

  char currency = '$';
  printf("The USD currency is: %c\n", currency);

  // Strings are available in C, but instead of a string data type, we use the char data type w/arrays to represent a string since they can store more than one value
  // To implement a string, we have to use double quotes ("") to store more than one character
  char name[] = "8BitSoftware";
  // To print the new array (string), we use the format specifier %s (for string)
  printf("Hello %s!\n", name);

  char food[] = "Pizza";
  printf("Your favorite food is: %s\n", food);

  // You can store digits within a "string". however they are treated as characters and not numbers
  char email[] = "fake123";
  printf("Your email is; %s@website.com\n", email);

  // To work with Boolean data types, you have to include the following header file: #include <stdbool.h> (meaning standard boolean)
  // Boolean data types are binary and can only exist in one of two states: True (1) or False (0)
  bool isOnline = true; // This can also be written as "bool isOnline = 1;"
  // To display a cool the format specifier is %d, and the output would return as either 1 (true) or 0 (false)
  printf("The user is online: %d\n", isOnline); // Prints "The user is online: 1"

  bool isOnline = false; // This can also be written as "bool isOnline = 0;"
  printf("The user is online: %d\n", isOnline); // Prints "The user is online: 0"

  // Booleans are typically left internal and are used in deicsion logic (like if statements)
  if (isOnline = true) {
    // You cannot use print even when you aren't referencing a variable!!!
    printf("You are ONLINE");
  } else {
    printf("You are OFFLINE");
  }

  return 0;
}