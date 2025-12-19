import sys

name = sys.argv[1]

print("\n Profile Information:")
print()

print( name.lower() + "@company.com")

''' ✅ QUESTION 2: TYPE CASTING + INPUT (MOST FREQUENT)

Write a Python program that:

Takes two values from the user
Converts them into integers
Prints:
Sum
Difference
Product
Floor division result '''

num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))

print("Sum of the two numbers is: " , num1+num2)
print("Difference of Two numbers is : ", num1-num2)
print("Product of Two numbers is: " ,num1*num2)
print("Floor Division of Two numbers is: ", num1//num2)

# QUESTION 3: MEMBERSHIP + LOGICAL OPERATORS

data = "Python Developer"

print("python" in data and "java" not in data)

# ✅ QUESTION 4: IDENTITY vs EQUALITY

a = [1,2,3]
b = [1,2,3]
c=a

print(a==b)
print(a is b)
print(a is c)