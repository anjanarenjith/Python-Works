# for n in range(10):
#     print(n)

# print('second loop')
# for n in range(1,11):
#     print(n)

# for n in range(1,5):
#     print('*'*n)
# for n in range(100,201):
#     if n%2==0:
#         print(n)
# for n in range(1,6):
#     print('*'*n)

# for n in range(5,0,-1):
#     print('*'*n)

# x = 5
# for n in range(5):
#     print('*'*x)
#     x-=1

# for x in range(0,100,2):
#     print(x)

# n = 1
# while n<=10:
#     print(n)
#     n+=1


# n=1
# while n<=6:
#     print('*'*n)
#     n+=1

# n = 6
# while n >= 1:
#     print('*' * n)
#     n -= 1

#break
# n=1
# while n<=10:
#     if(n==4):
#         n+=1
#         break #skip an iteration
#     print(n)
#     n+=1

#continue
# n=1
# while n<=10:
#     if(n==4):
#         n+=1
#         continue #skip an iteration
#     print(n)
#     n+=1

# #iteration 1
# n=1
# 1<=10->True
# 1==4->False
# n=2

# #iteration 2
# n=2
# 2<=10->True
# 2==4->False
# n=3

# #iteration 3
# n=3
# 3<=10->True
# 3==4->False
# n=4

# #iteration 4
# n=4
# 4<=10->True
# 4==4->true
# When i becomes 4, continue skips print(n). The loop then continues with 5.

# o/p
# 1 2 3 5 6 7 8 9 10

# for i in range(1, 6):
#     if i == 3:              
#         continue
#     print("*" * i)

# o/p
# *
# **
# ****
# *****

#find the sum of a number
# n=int(input("enter the number:"))
# sum=0
# while n>0:
#     r = n%10
#     sum +=r
#     n //=10
# print(f"sum is {sum}")

# #iteration 1
# n = 487
# sum=0
# r=487%10=7
# sum=0+7=7
# n=487//10=48

# #iteration 2
# n = 48
# sum=7
# r=48%10=8
# sum=7+8=15
# n=48//10=4


# #iteration 3
# n = 4
# sum=15
# r=4%10=4
# sum=15+4=19
# n=4//10=0

#collections

numbers = [45,870,110,134,1550,155]
print(numbers)
print(type(numbers))
print(len(numbers))
print(numbers[3])
print(numbers[0:3])
print(numbers[0:5:2])
print(numbers[::-1])
print(numbers[-1])

numbers[2] =1

print(numbers)

for n in numbers:
    print(n)
print('even numbers')
for n in numbers:
    if n%2 ==0:
        print(n)










