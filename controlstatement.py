#Decision making statements
# if statements
# if-else statement
# if-elif-else statements
# Nested if

#if condition:
#   block of code
    

#age=18
#if age>=18:
#    print('Adult')

#if age>=17:
#    print('Adult')
#else:
#  print('child')
#print('after if block')

#if age > 0 and age < 13:
#   print('child')
#elif age>=13 and age<20:
#    print('teeneger')
#elif age>=20 and age<60:
#    print('adult')
#elif age >=60:
#    print('senior citizen')

#else:
#    print('invalid entry')

#age = int(input("enter your age:"))
#mark = int(input("enter the marks:"))
#if age>= 18:
#   print("Age required satisfied..")
#    if mark >=50:
#       print("Admission Approved")
#    else:
#       print("Admission rejected insufficient marks")
#else:
#    print("Admission rejected: age Equirements is not satisfied18")

#day=int(input("enter the day:"))
#match day:
   # case 1:
      #  print('Monaday')
   # case 2:
    #        print('tuesday')
   # case 3:
    #            print('Wednesday')
    #case _:
    #          print('inavalid entry')

#mark and grade
#mark = int(input("enter the marks:"))
#if mark >90 and mark <=100:
 #   print("A+")
#elif mark >80 and mark <=90:
#     print("A")
# elif mark >70 and mark <=80:
#     print("B+")
# elif mark >60 and mark <=70:
#     print("B")
# elif mark >50 and mark <=60:
#     print("C")
# elif mark >=40 and mark <=50:
#     print("D")
# elif mark >40 and mark >=0:
#     print("E")
# else:
#     print("invalid marks entry...")

day = "monday"

match day.capitalize():
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")

    case "Sunday" | "Saturday":
        print("Weekend")

    case _:
        print("Invalid")



