a=10
b=3 
#addition
#print(a+b)
#substraction
#print(a-b)
#multiplication
#print(a*b)
#division
#print(a/b)
#Floor division
#print(a//b)
#modulous
#print(a%b)
#Exponentiation
#print(a**b)
#print(type(a))
#print(int("544644f"))
#print(int(True))
#print(int(False))
#a = int(input("Enter a number:"))
#b = int(input("enter a number"))
#print(a%b)
#print(17//5)
#print(15+8*3)
#print(2**3**2)
#print(8+2**3-9)

#a = int(input("enter the number"))
#print(1*a)
#print(2*a)
#print(3*a)
#print(4*a)
#print(5*a)
#print(6*a)
#print(7*a)
#print(8*a)
#print(9*a)
#print(10*a)

#Assignment operator

#name = "jithu"
#a = 10
#a += 8
print(a)

a -= 5
print(a)

a *= 2
print(a)

a /= 2
print(a)

a **= 2
print(a)

a %= 2
print(a)


#comparison operator

x=10
y=10
print(x>y)

x=10
y=15
print(x<y)

x=10
y=15
print(x>=y)

x=10
y=10
print(x==y)

x=7
y=8
print(x!=y)

#logical operator

age = 19
voter_id = True
print(age>=18 and voter_id==True)

pan_card = False
print(voter_id or pan_card)

print("hello\nworld")
print(age,pan_card,voter_id)
print(age,pan_card,voter_id,sep='\n')

#identity operator
p = 10
q = 10
r = [89,73,14]
s = [89,73,14]
print(p==q)
print(p is q,end=' ')
print(r is s)
print(id(r))
print(r is r)
mark = 45
grade = mark>40 and "A"
print("hai" and "hello")
print(1 and "hello")
print(0 and "hello")

#memeber ship operator

print("p" in "python")
print("P" in "python")
print(4 not in[4,8,7,6])

# print(bool(True))
#print(bool(False))
print(bool("hello"))
print(bool(""))
print(bool(5456))
print(bool(-5456))
print((bool(0)))
print(bool(["a","b"]))
print(bool([]))

# Bitwise operators

m = 5
n = 3

# &
print(m & n)  # 1
print(m | n)
print(m ^ n)
print(~m)     # ~5 = -6
print(~n)     # ~3 = -4

# ~n = -(n+1)

print(~89)    # -90


# 0000
# 0001
# 0010

# 2**3   2**2   2**1   2**0
#   8      4      2      1
#   1      1      0      0   ==> 12
#   0      0      0      1


# 0    1    0    1    ==> 5 &
# 0    0    1    1    ==> 3
# --------------------
# 0    0    0    1


# 0    1    0    1    ==> 5 |
# 0    0    1    1    ==> 3
# --------------------
# 0    1    1    1


# 0    1    0    1    ==> 5 ^ (XOR)
# 0    0    1    1    ==> 3
# --------------------
# 0    1    1    0
