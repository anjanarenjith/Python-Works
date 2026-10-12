# Exercise 1: Traffic Light Simulator
# color = input("Enter the color:")
# if color == "red":
#     print("Stop")
# elif color == "yellow":
#     print("Slow down")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid color")

# Exercise 2: Even or Odd?
# number = int(input("enter the number:"))
# if number % 2 == 0:
#     print("Even numbers")
# else:
#     print("Odd")

# Basic If-Else  Questions

# 1.Write a program that checks if a number is positive, negative, or zero
# n = int(input("enter the number:"))
# if n > 0 :
#     print("positive number")
# elif n < 0:
#     print("Negative number")
# else:
#     print("Zero")

# 2.Check if a given number is even or odd.
# number = int(input("enter the number:"))
# if number % 2 == 0:
#     print("Even numbers")
# else:
#     print("Odd") 

# 3.Determine if a user is eligible to vote (age >= 18).
# age = int(input("enter the age:"))
# if age >= 18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")
# 4.Write a program that takes a temperature input and prints "Cold" if it's below 20°C, "Warm" if between 20-30°C, and "Hot" if above 30°C

# temp = float(input("Enter temperature: "))
# if temp < 20:
#     print("Cold")
# elif temp <= 30:
#     print("Warm")
# else:
#     print("Hot")

# 5. leap year
# year = int(input("Enter a year: "))
# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# Nested If Questions
# 6.Take input for marks and print grades as per the following

# marks = int(input("Enter marks: "))

# if marks >= 0 and marks <= 100:
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 80:
#         print("Grade B")
#     elif marks >= 70:
#         print("Grade C")
#     elif marks >= 60:
#         print("Grade D")
#     else:
#         print("Grade F")
# else:
#     print("Invalid marks")

# 7.Write a program to check if a number is positive and even; otherwise, print "Not positive or not even."

# n = int(input("Enter a number: "))
# if n > 0:
#     if n % 2 == 0:
#         print("Positive and even")
#     else:
#         print("Not positive or not even")
# else:
#     print("Not positive or not even")

# 8.Given three numbers, find the largest number among them.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b:
#     if a >= c:
#         print("Largest:", a)
#     else:
#         print("Largest:", c)
# else:
#     if b >= c:
#         print("Largest:", b)
#     else:
#         print("Largest:", c)


# If-Elif-Else Questions

# 9.A shop gives discounts based on purchase amount:

# amount = float(input("Enter purchase amount: "))
# if amount > 5000:
#     discount = amount * 20 / 100
# elif amount >= 2000:
#     discount = amount * 10 / 100
# else:
#     discount = 0
# bill = amount - discount
# print("Discount:", discount)
# print("Final bill:", bill)

# 10.Convert a numerical day (1-7) into its corresponding weekday name

# day = int(input("Enter a number (1-7): "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid day")

# For Loop Questions
# 1.Print numbers from 1 to 10 using a for loop.
# for n in range (1,11):
#     print(n)
# 2.Print the multiplication table of a given number.
# n = int(input("enter the number:"))
# for i in range(1,11):
#     print(n*i)

# 3.Find the sum of all numbers from 1 to n.
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print("Sum:", total)

# 4. Print the first n Fibonacci numbers.

# n = int(input("Enter how many numbers: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# 5.Print a pattern like:
# for i in range(1, 5):
#     print("*" * i)

# 6.Reverse a string using a loop
# name = input("Enter a name: ")
# reverse = ""
# for ch in name:
#     reverse = ch + reverse
# print("Reverse:", reverse)

# 7.Print all even numbers from 1 to 50
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# While Loop
# 8.Print numbers from n to 1 using a while loop.
# n = int(input("Enter a number: "))
# while n >= 1:
#     print(n)
#     n = n - 1
# 9. factorial
# n = int(input("Enter a number: "))
# fact = 1
# while n > 1:
#     fact = fact * n
#     n = n - 1
# print("Factorial:", fact)

# 10.Print all digits of a number separately.
# n = int(input("Enter a number: "))
# if n < 0:
#     n = -n
# while n > 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10
# 11.Count the number of digits in a given number
# n = int(input("Enter a number: "))
# n = abs(n)
# count = 0
# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         count = count + 1
#         n = n // 10
# print("Number of digits:", count)
# 12.Keep taking user input until they enter "exit".
# while True:
#     text = input("Enter something (or exit): ")
#     if text == "exit":
#         break
#     print("You entered:", text)
# print("Program stopped")

# Loop Control Statements

# 13.Use break to stop the loop when a number is found in a list.

# numbers = [10, 20, 30, 40, 50]
# target = int(input("Enter number to find: "))
# for n in numbers:
#     if n == target:
#         print("Number found")
#         break
# else:
#     print("Number not found")
# 14.Use continue to skip printing even numbers from 1 to 20.
# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)
# 15.Use pass inside a loop without affecting its flow.
# for i in range(1, 6):
#     if i == 3:
#         pass
#     print(i)

# # Match Statements

# # 1.Day classifier
# day = int(input("Enter day (1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid day")

# 2. Simple calculator

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# match op:
#     case "+":
#         print("Result:", a + b)
#     case "-":
#         print("Result:", a - b)
#     case "*":
#         print("Result:", a * b)
#     case "/":
#         if b != 0:
#             print("Result:", a / b)
#         else:
#             print("Cannot divide by zero")
#     case _:
#         print("Invalid operator")

# 3. Grade checker using guards

# marks = int(input("Enter marks: "))

# match marks:
#     case x if 90 <= x <= 100:
#         print("Grade A")
#     case x if 80 <= x < 90:
#         print("Grade B")
#     case x if 70 <= x < 80:
#         print("Grade C")
#     case x if 60 <= x < 70:
#         print("Grade D")
#     case x if 0 <= x < 60:
#         print("Grade F")
#     case _:
#         print("Invalid marks")

# 4. HTTP status handler

# status = int(input("Enter status code: "))
# match status:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case x if 500 <= x <= 599:
#         print("Server Error")
#     case x if x >= 400:
#         print("Client Error")
#     case _:
#         print("Other Status")
# 5. Chess board color

# row = int(input("Enter row (1-8): "))
# col = int(input("Enter column (1-8): "))

# if 1 <= row <= 8 and 1 <= col <= 8:
#     match (row % 2, col % 2):
#         case (1, 1) | (0, 0):
#             print("Black")
#         case (1, 0) | (0, 1):
#             print("White")
# else:
#     print("Invalid position")
# 6. Command parser

# cmd = ["add", 5, 3]
# match cmd:
#     case ["add", a, b]:
#         print("Result:", a + b)
#     case ["quit"]:
#         print("Program stopped")
#     case _:
#         print("Invalid command")
# 7. File type checker

# filename = input("Enter filename: ")
# parts = filename.split(".")

# match parts:
#     case [name, "jpg" | "png"]:
#         print("Image file")
#     case [name, "py"]:
#         print("Python file")
#     case _:
#         print("Unknown file type")
# 8. Shape area calculator

# shape = ("circle", 5)
# match shape:
#     case ("circle", r):
#         print("Area:", 3.14 * r * r)
#     case ("rect", l, b):
#         print("Area:", l * b)
#     case _:
#         print("Invalid shape")


















    



