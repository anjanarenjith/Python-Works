# 1. Student Marks 
# marks = []
# for i in range(5):
#     mark = int(input("Enter marks of student: "))
#     marks.append(mark)
# print("Student marks:", marks)
# print("Highest mark:", max(marks))
# print("Lowest mark:", min(marks))
# count = 0
# for mark in marks:
#     if mark > 50:
#         count += 1
# print("Students scored above 50:", count)

# 2. Even and Odd Numbers 

# numbers = []
# for i in range(10):
#     number = int(input("Enter a number: "))
#     numbers.append(number)
# print("The numbers:", numbers)
# even = []
# odd = []
# for number in numbers:
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 3. Positive, Negative and Zero 

# numbers = []
# for i in range(10):
#     number = int(input("Enter a number: "))
#     numbers.append(number)
# positive = 0
# negative = 0
# zero = 0
# for number in numbers:
#     if number > 0:
#         positive += 1
#     elif number < 0:
#         negative += 1
#     else:
#         zero += 1
# print("Numbers:", numbers)
# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Zeros:", zero)

# 4. Search an Element 

# numbers = []

# for i in range(5):
#     number = int(input("Enter a number: "))
#     numbers.append(number)
# search = int(input("Enter a number to search: "))
# if search in numbers:
#     print("Number found at position:", numbers.index(search) + 1)
# else:
#     print("Number not found")

# 5. Shopping Cart 

# prices = []
# n = int(input("How many products do you want to add? "))
# for i in range(n):
#     price = float(input("Enter product price: "))
#     prices.append(price)
# total = sum(prices)
# if total > 5000:
#     discount = total * 10 / 100
# else:
#     discount = 0
# final_amount = total - discount
# print("Product prices:", prices)
# print("Total amount:", total)
# print("Discount:", discount)
# print("Final amount:", final_amount)

# 6. Number Analyzer 

# numbers = []
# for i in range(10):
#     number = int(input("Enter a number: "))
#     numbers.append(number)
# total = sum(numbers)
# average = total / len(numbers)
# largest = max(numbers)
# smallest = min(numbers)
# even = 0
# odd = 0
# for number in numbers:
#     if number % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Numbers:", numbers)
# print("Sum:", total)
# print("Average:", average)
# print("Largest number:", largest)
# print("Smallest number:", smallest)
# print("Even numbers count:", even)
# print("Odd numbers count:", odd)

# 7. Remove Negative Numbers 

# numbers = []
# n = int(input("How many numbers do you want to enter? "))
# for i in range(n):
#     number = int(input("Enter a number: "))
#     numbers.append(number)
# positive = []
# for number in numbers:
#     if number > 0:
#         positive.append(number)
# print("Original list:", numbers)
# print("Positive numbers list:", positive)

# 8. Find Duplicate Values 

# numbers = []

# for i in range(10):
#     number = int(input("Enter a number: "))
#     numbers.append(number)
# duplicates = []
# for number in numbers:
#     if numbers.count(number) > 1 and number not in duplicates:
#         duplicates.append(number)
# print("Original list:", numbers)
# print("Duplicate numbers:", duplicates)

# 9. Write a Python program to check whether a given number is a palindrome. 

# number = int(input("Enter a number: "))
# original = number
# reverse = 0
# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10
# if original == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")

# 10. Write a Python program to check whether a given number is an Armstrong number.  

# number = int(input("Enter a number: "))
# original = number
# digits = len(str(number))
# total = 0
# while number > 0:
#     digit = number % 10
#     total = total + digit ** digits
#     number = number // 10
# if total == original:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# 11. Write a Python program to check whether a given number is a prime number.  

# number = int(input("Enter a number: "))
# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")

# 12. Write a Python program to find the largest digit in a given number.

number = int(input("Enter a number: "))
largest = 0
while number > 0:
    digit = number % 10
    if digit > largest:
        largest = digit
    number = number // 10
print("Largest digit:", largest)











