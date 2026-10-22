n=int(input("enter the number:"))
rev = 0
while n > 0:
    r = n % 10
    rev = (rev*10)+r
    n//=10
else:
    print("Reverse is",rev)

# Iteration 1:
# - r = 487 % 10 = 7
# - rev = (0 * 10) + 7 = 7
# - n = 487 // 10 = 48
# Iteration 2:
# - r = 48 % 10 = 8
# - rev = (7 * 10) + 8 = 78
# - n = 48 // 10 = 4
# Iteration 3:
# - r = 4 % 10 = 4
# - rev = (78 * 10) + 4 = 784
# - n = 4 // 10 = 0