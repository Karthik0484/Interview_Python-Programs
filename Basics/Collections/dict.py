'''🔹 DICTIONARY – Interview Questions (VERY IMPORTANT)
Q1. Student Grade System

Given student marks:
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 60
}
Create a new dictionary:

A → marks ≥ 85
B → marks ≥ 70
C → marks < 70'''

students = { "Alice": 85,"Bob": 72,"Charlie": 90,"David": 60}
grades={}

for name,marks in students.items():
    if marks >= 85:
        grades[name] = 'A'
    elif marks >= 70:
        grades[name] = 'B'
    else:
        grades[name]='C'

print(grades)

'''Q2. Login Attempt Tracker

Given login logs:
logs = ["Alice", "Bob", "Alice", "Alice", "Bob"]
Create a dictionary showing number of login attempts per user.'''

logs = ["Alice", "Bob", "Alice", "Alice", "Bob"]
login_count={}

for name in logs:
    if name in login_count:
        login_count[name] += 1
    else:
        login_count[name] = 1
print(login_count)

'''Q3. Find Max Value Key
Find the student who scored highest marks from a dictionary. '''

students = { "Alice": 85,"Bob": 72,"Charlie": 90,"David": 60}
max_mark = 0
top_students = None

for name,marks in students.items():
    if marks > max_mark:
        top_students = name
        max_mark = marks
print("Top student: ",top_students)
print("Marks: ",max_mark)

'''Q4. Inventory Update

You are given:
inventory = {"apple": 10, "banana": 5}
sales = {"apple": 3, "banana": 2}

Update inventory after sales.'''

inventory = {"apple": 10, "banana": 5}
sales = {"apple": 3, "banana": 2}

for items,qty in sales.items():
    if items in inventory:
        inventory[items] -= qty

print(inventory)



