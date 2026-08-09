# Exercise 11: Invoice Display - Display an invocie using a function
# 16 - 18 Notes

def invoice_display(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

username = input("What is your name? ")
amount = float(input("How much is owed? "))
due_date = input("When the amount due? ")
print()

invoice_display(username, amount, due_date)