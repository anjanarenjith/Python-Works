# key-value pairs
student = {
    "name":"Amal",
    "age":18,
    "rno":2,
    "course":"Bca" 
   
}
print(student)
print(type(student))
print(student["age"])
student["name"] = "Amal Siby"
print(student["name"])
student["email"] = "amal@gamil.com"
print(student)
print("Bca" in student)
for x in student:
    print(student[x])

    #functions

print(student['age'])
print(student.get('age'))
print(student.get('agee'))
print(student.get('agee',20))
student.update({"hobbies":("Reading","Writing")})
student.update({"rno":4})
student.setdefault("course","BBA")
student.pop('rno')

print(student.values())
print(student.keys())
print()
for key,value in items:
    print(f"{key}: {value}")


