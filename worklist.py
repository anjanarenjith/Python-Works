# 1. Find the Largest Element 
# numbers = [10, 5, 25, 8, 15]
# largest = numbers[0]
# for i in range(1, len(numbers)):
#     if numbers[i] > largest:
#         largest = numbers[i]
# print("The largest element is:", largest)

# 2. Find the Smallest Element 
# numbers = [10, 5, 25, 8, 15] 
# smallest = numbers[0]
# for i in range(1, len(numbers)):
#     if numbers[i] < smallest:
#         smallest = numbers[i]
# print("The smallest element is:", smallest)

# 3. Find Sum of All Elements 
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for i in range(0, len(numbers)):
#     total = total + numbers[i]
# print("The sum of all numbers:", total)

# 4. Find Average of Elements
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for i in range(0, len(numbers)):
#     total = total + numbers[i]
# average = total / len(numbers)
# print("The average is:", average)

# 5.Reverse a List Without Using reverse()
# numbers = [1, 2, 3, 4, 5]
# i = len(numbers) - 1
# while i >= 0:
#     print(numbers[i], end=" ")
#     i -= 1

# Logic-Based List Questions

# 1. Remove Duplicates

# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# 2. Find the Second Largest Number

# numbers = [10, 20, 50, 40, 30]
# numbers.sort()
# print("Second largest:", numbers[-2])

# 3. Separate Even and Odd Numbers

# numbers = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []
# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 4. Find Common Elements Between Two Lists

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common = []
# for num in list1:
#     if num in list2:
#         common.append(num)
# print("Common elements:", common)

# 5. Merge Two Lists Without Duplicates

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# merged = []

# for num in list1 + list2:
#     if num not in merged:
#         merged.append(num)
# print(merged)
# Nested List Questions

# 1. Sum of All Elements in a Matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# total = 0

# for row in matrix:
#     for num in row:
#         total += num
# print("Sum:", total)

# # 2. Find the Largest Element in a Matrix

# matrix = [
#     [1, 2, 3],
#     [10, 5, 6],
#     [7, 8, 9]
# ]
# largest = matrix[0][0]
# for row in matrix:
#     for num in row:
#         if num > largest:
#             largest = num
# print("Largest element:", largest)




