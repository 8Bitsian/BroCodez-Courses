# Python Note Template

## Main File Setup

### File Header comment block for starting new main.py files:
Thank you @omp3policeo on Twitch for back-tick suggestion! </br>
If you add python after the back-ticks then markdown will read the code inside as Python.
```cpp
// Project #: Name - Uses Notes #
// File: filename.cpp
// Description: Brief description of this file
// Uses: List of related files, classes, or modules
```

### Main method syntax for starting new main.cpp files:
```cpp
// Standard-library includes
# include <iostream>
# include <string>

// Third-party or local library imports
# include "header_name.hpp"

// Describe what this function does
void function_name() {
}

// Runs the main program
int main() {
    // std:cout << "Running program...\n";
    function_name();
    // std:cout << "Program finished.\n";
    return 0;
}
```

---
## Header/Source File Setup

### Basic header syntax for starting new module.hpp files:
```hpp
// Project #: Project Name
// File: module_name.hpp
// Description: Brief description of this module

#pragma once

// Standard-library includes
#include <string>

# Constant
inline constexpr int CONSTANT_NAME = 0;

# Function Declaration
void function_name(int parameter);
```

### Basic source syntax for starting new module.cpp files:
```cpp
// Project #: Project Name
// File: module_name.cpp
// Description: Brief description of this module

#include "module_name.hpp"

// Function Definition
void funciton_name(int parameter) {
}
```

---
## Class Setup

### Parent class header syntax for parent.hpp:
```hpp
// Project #: Project Name
// File: parent_name.hpp
// Description: Brief description of this module

#pragma once

// Standard-library includes
#include <string>

# Class Declaration
class Parent {
    public:
        // Constructor
        explicit Parent(int pVar);

        // Virtual Deconstructor
        virtual -Parent() = default;

        // Instance Method
        virtual void function_name();

        // Getter Method
        sid::string getName() const;

    protected:
        // Instance Variable
        int pVar_;

    private:
        // Class Variable shared by all Parent objects
        inline static constexpr const char* className_ = "Parent";
};
```

### Parent class source syntax for parent.cpp:
```cpp
#include "parent_name.hpp"

Parent::Parent(int pVar) : pVar_(pVar) {
}

void Parent::function() {
}

std::string Parent::getName() const {
    return class_name_;
}
```

### Child class header syntax for child.hpp:
```hpp
// Project #: Project Name
// File: parent_name.hpp
// Description: Brief description of this module

#pragma once

#include "parent.hpp"

# Class Declaration
class Child : public Parent {
    public:
        // Constructor
        Child(int pVar, int cVar);

        // Override an inherited method
        void function_name() override;

        // Getter Method
        int get_C_Var() const;

        // Setter Method
        void set_C_Var(int newVar);

    private:
        int cVar_;
};
```

### Child class source syntax for child.cpp:
```cpp
#include "child_name.hpp"

Child::Child(int pVar, int cVar)
    : Parent(pVar), cVar_(cVar) {
}

void Child::function() {
}

int Child::getCVar() const {
    return cVar_;
}

void Child::setCVar(int newVar) {
    cVar_ = newVar;
}
```
