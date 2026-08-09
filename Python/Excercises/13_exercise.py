# Exercise 13: Generate Phone Number - Generate a phoen number by passing area code, and numbers
# 20 Notes

def get_phone(country, area, f_digits, l_digits):
    return f"+{country} ({area}) {f_digits}-{l_digits}"

arg1 = int(input("Enter Country Code: "))
arg2 = int(input("Enter Area Code: "))
arg3 = int(input("Enter 3 Digits: "))
arg4 = int(input("Enter 4 Digits: "))

phone_num = get_phone(country = arg1, area = arg2, f_digits = arg3, l_digits = arg4)

print(phone_num)