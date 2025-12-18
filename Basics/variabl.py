'''QUESTION 1: USER INPUT + TYPE CASTING (MOST COMMON)

Problem:

Write a Python program that:

Takes two numbers from the user
Converts them to integers
Prints their sum '''

x = int(input("Enter the value: "))
y = int(input("Enter the value: "))
print("Sum :",x+y)
print()

# QUESTION 2: VARIABLE SCOPE (LEGB RULE – FAVOURITE)

x = 100

def func():
    x = 50
    print(x)
func()

print(x)
print()

''' QUESTION 3: GLOBAL KEYWORD (VERY FREQUENT)

Problem:

Write a Python program where:

A global variable count starts with value 0
A function increments count by 1
Print the final value of count '''

count = 0

def incre():
    global count
    count += 1
    print(count)

incre()
print()

''' QUESTION 4: TYPE CHECKING + INPUT (TRICKY)

Problem:

Write a program that:

Takes input from the user
Checks whether the input is a number or a string
Prints the result '''

x = input("Enter the value: ")

if x.isdigit():
    print('Number')

else:
    print("String")

print()

# QUESTION 5: OUTPUT PREDICTION (VERY COMMON)

a = "10"
b = 20
print(a * b)


