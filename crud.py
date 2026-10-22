# names=["Amal","Karthik"]
# while True:
#     choice=int(input("1. Add a name\n2.Display names\n3.Edit a name\n4.Delete a name\n5.Exit\nEnter your choice: "))
#     match choice:
#         case 1:
#             name=input("Enter a name: ")
#             names.append(name)
#         case 2:
#             print(format("Sl.No.","<10"),format("Name","<10"))
#             print("-"*20)
#             count=1
#             for x in names:
#                 print(format(count,"<10"),format(x))
#                 count+=1
#         case 3:
#             print(format("Sl.No.","<10")),format("Name")
#             print("-"*20)
#             count=1
#             for x in names:
#                 print(format(count,"<10"),format(x))
#                 count+=1
#             edit_index=int(input("Enter the Sl. No. of the name you want to edit: ")) -1
#             new_name=input("Enter the new name: ")
#             names[edit_index]=new_name
#         case 4:
#             print(format("Sl.No.","<10")),format("Name")
#             print("-"*20)
#             count=1
#             for x in names:
#                 print(format(count,"<10"),format(x))
#                 count+=1
#             delete_index=int(input("Enter the Sl. No. of the name you want to delete: ")) -1
#             names.pop(delete_index)
#         case 5:
#             print("exiting...")
#             break
#         case _:
#             # print("Invalid choice")


# compact if statement

# number = 3
# is_even_or_odd = "Even" if number % 2 == 0 else "Odd"
# print(is_even_or_odd)

