'''🔹 TUPLE – Interview Questions
Q6. Immutable Record Check

You are given student records as tuples:
records = [("Alice", 85), ("Bob", 90), ("Alice", 95)]

Find all students with marks above 90. '''
records = [("Alice", 85), ("Bob", 90), ("Alice", 95)]

for record in records:
    name,marks = record
    if marks > 90:
        print(name,marks)

'''


Q7. Tuple Unpacking (HR Favorite)

Given employee details:
employee = ("Karthik", 20, "Python Developer")

Unpack and print in this format:
Name: Karthik
Age: 20
Role: Python Developer'''

employee = ("Karthik", 20, "Python Developer")
name,age,role=employee

print("Name: ",name)
print("Age: ",age)
print("Role: ",role)



