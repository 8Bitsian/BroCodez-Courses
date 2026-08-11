# Exercise 15: Various Comprehensive Lists
# 22 - 24 Notes

fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)

upper_fruits = [(fruit.upper()) for fruit in fruits]
print(upper_fruits)

fruit_chars = [(fruit[0]) for fruit in fruits]
print(fruit_chars)
print()

numbers = [1, -2, 3, -4, 5, -6, -7, 8]

positive_nums = [(num) for num in numbers if (num >= 0)]
print(positive_nums)

negative_nums = [(num) for num in numbers if (num < 0)]
print(negative_nums)

even_nums = [(num) for num in numbers if (num % 2 == 0)]
print(even_nums)

odd_nums = [(num) for num in numbers if (num % 2 == 1)]
print(odd_nums)
print()

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [(grade) for grade in grades if (grade >= 60)]
print(passing_grades)

failing_grades = [(grade) for grade in grades if (grade < 60)]
print(failing_grades)