# l2=[45,86,97,41,37,54,20,36]
# even_number =[]
# for x in l2:
#     if x % 2== 0:
#         even_number.append(x)
# print(even_number)

# l1 = [45,86,97,41,37,54,20,36]

# new_list =[x for x in l1]
# even_number =[x for x in l1 if x%2==0]
# squared_number = [x * x for x in l1]
# print(new_list)
# print(squared_number)
# print(even_number)

# l2 = [45,86,97,41,37,54,20,36]
# ['odd','even','odd','odd','odd','even',even',even'] how to print this?

l2 = [45, 86, 97, 41, 37, 54, 20, 36]
result = ['even' if x % 2 == 0 else 'odd' for x in l2]
print(result)