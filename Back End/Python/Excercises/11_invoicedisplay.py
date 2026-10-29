# Exercise 11: Invoice Display - Note 18
# Display an invoice using a function

def invoice_display(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

username = input("What is your name? ")
amount = float(input("How much is owed? "))
due_date = input("When the amount due? ")
print()

invoice_display(username, amount, due_date)
