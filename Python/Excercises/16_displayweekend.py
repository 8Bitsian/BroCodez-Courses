# Exercise 16: Display The Weekend - Note 25
# Use a match-case (switch) statement to display if it is the weekend

def is_weekend(day):
    match day:
        # Utilize the OR (|) logical operator to condense code
        case "saturday" | "sunday":
            return True
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False      
        case _: # The underscore is a wildcard which acts as the defualt (else) statement
            return "Not a valid day..." 

# Incldued the .lower() method for input validation
day = input("What day is it? ").lower()

print(is_weekend(day))
