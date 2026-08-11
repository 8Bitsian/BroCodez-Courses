# Match-case Statement (Switch)

# Match-case, or `switch`, statements are an alternative to using many `elif` statements.
# Switch statements were added in Python v.3.10.
# Code blocks are executed if a value matches a `case`
# Switch statements are often cleaner and the syntax is more readable

# def day_of_week(day):
#     if day == 1:
#         return "It's Saturday"
#     elif day == 2:
#         return "It's Monday"
#     elif day == 3:
#         return "It's Tuesday"
#     elif day == 4:
#         return "It's Wednesday"
#     elif day == 5:
#         return "It's Thursday"
#     elif day == 6:
#         return "It's Friday"
#     elif day == 7:
#         return "It's Saturday"
#     else:
#         return "Not a valid day..."

def day_of_week(day):
    match day:
        case 1:
            return "It's Saturday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Sunday"        
        case _: # The underscore is a wildcard which acts as the defualt (else) statement
            return "Not a valid day..." 

day = int(input("What day is it? (1-7) "))

print(day_of_week(day))