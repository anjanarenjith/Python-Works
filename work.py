# To add two numbers

# a = int(input("Enter the first number:"))
# b = int(input("enter the second number:"))
# print(a + b)

# To find the difference between two numbers

# a = int(input("Enter the first number:"))
# b = int(input("enter the second number:"))
# print(a - b)

# To multiply three numbers.

# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c = int(input("Enter the third number:"))
# print(a * b * c)

# To divide one number by another

# a = int(input("Enter the first number:"))
# b = int(input("enter the second number:"))
# print(a / b)

# To calculate the square of a number

# a=int(input("enter the number:"))
# print(a ** 2)

# To calculate the cube of a number. 

# a=int(input("enter the number:"))
# print(a ** 3)

# To calculate the average of three numbers

# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c = int(input("Enter the third number:"))
# average = (int(input(a + b + c) / 3))
# print(average)

# Price of 5 notebooks

# price = int(input("Enter price of one notebook: "))
#total = price * 5
# print(total)

# Quotient and remainder
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Quotient =", a // b)
# print("Remainder =", a % b)

# 10. A shop has 47 chocolates. If each box holds 6 chocolates,calculate:
# a)The number of completely filled boxes.
# b)The number of chocolates left over. 

# chocolates = 47
# box = 6
# print("Complete boxes =", chocolates // box)
# print("Chocolates left =", chocolates % box)

#11. Write a program to convert a given number of minutes into complete hours and remaining minutes. 

# minutes = int(input("Enter minutes: "))
# print("Hours =", minutes // 60)
# print("Remaining minutes =", minutes % 60)

# 12.Write a program to convert 367 seconds into minutes and remaining seconds.

#seconds = 367
#print("Minutes =", seconds // 60)
#print("Remaining seconds =", seconds % 60)

# 13.A teacher wants to distribute 53 students into groups of 8. Calculate the number of complete groups and the students left over. 

students = 53
group = 8
#print("Complete groups =", students // group)
#print("Students left =", students % group)

#14. Write a program to extract the last digit of a positive integer using the modulus operator

#number = int(input("Enter a number: "))
#print(number % 10)

#15. Write a program to remove the last digit of a positive integer using floor division.

#number = int(input("Enter a number: "))

#print(number // 10)

#16. Shopping bill: A customer buys 3 pens costing ₹15 each and 2 notebooks costing ₹40 each. Calculate the total bill. 

#pens = 3 * 15
#notebooks = 2 * 40
#total = pens + notebooks
#print("Total bill =", total)

# 17.Salary calculation: An employee earns ₹800 per day. Calculate their salary for 26 working days. 

#daily_salary = 800
#days = 26
#salary = daily_salary * days
#print("Salary =", salary)

#18. Distance conversion: Convert a distance given in kilometers into meters and centimeters. 
#km = float(input("Enter distance in kilometers: "))
#meters = km * 1000
#centimeters = km * 100000
#print("Meters =", meters)
#print("Centimeters =", centimeters)

#19.Rectangle: Accept the length and width of a rectangle and calculate its area and perimeter. 

#length = int(input("Enter length: "))
#width = int(input("Enter width: "))
#area = length * width
#perimeter = 2 * (length + width)
#print("Area =", area)
#print("Perimeter =", perimeter)

#20. Simple interest: Accept the principal amount, annual interest rate, and time in years. Calculate the simple interest using: 

#p = float(input("Enter principal: "))
#r = float(input("Enter interest rate: "))
#t = float(input("Enter time: "))
#si = (p * r * t) / 100
#print("Simple Interest =", si)

#21. Bill sharing: Accept a restaurant bill and the number of friends. Calculate how much each friend should pay if the bill is shared equally. 

#bill = float(input("Enter restaurant bill: "))
#friends = int(input("Enter number of friends: "))
#each = bill / friends
#print("Each friend should pay =", each)

#22. Travel calculation: A car travels 180 km using 12 liters of fuel. Calculate its mileage in km per liter. 
#distance = 180
#fuel = 12
#mileage = distance / fuel
#print("Mileage =", mileage, "km/l")

# 23. Unit price: Accept the total price of a packet of rice and its weight in kilograms. Calculate the price per kilogram. 

#price = float(input("Enter total price: "))
#weight = float(input("Enter weight in kg: "))
#price_per_kg = price / weight
#print("Price per kg =", price_per_kg)

#24. Time conversion: Accept a total number of hours and convert it into complete days and remaining hours. 

#hours = int(input("Enter hours: "))
#days = hours // 24
#remaining_hours = hours % 24
#print("Days =", days)
#print("Remaining hours =", remaining_hours)

# 25. Power calculation: Accept a number and an exponent, then calculate the result using the ** operator. 

number = int(input("Enter number: "))
exponent = int(input("Enter exponent: "))
result = number ** exponent
print("Result =", result)  