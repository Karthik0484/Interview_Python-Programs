'''🔹 C. FUNCTIONS – 5 INTERVIEW QUESTIONS
Q1. Modular Billing System

Create functions:
calculate_tax(price)
apply_discount(price)
final_bill(price)'''

def calculate_tax(price):
    tax = price * 0.18
    return tax

def apply_discount(price):
    discount = price * 0.1
    return discount

def final_bill(price):
    tax = calculate_tax(price)
    discount_new = apply_discount(price)
    final = price + tax - discount_new
    return final

Bill = final_bill(100)
print("Final Bill: ", Bill)

'''👉 Each function must call another where required.
Q2. ATM System Using Functions

Create functions for:
deposit
withdraw
check balance
👉 Balance must persist across function calls.'''
balance = 0

def deposit(amount):
    global balance
    print(" Amount you deposit: ", amount)
    balance += amount
    return balance

def withdraw(amt):
    global balance
    if amt <= balance:
        print("Amount Withdrawn: ",amt)
        balance -= amt
    else:
        print("Insufficient Balance")
    return balance

def check_balance():
    return balance

deposit(1000)
withdraw(500)
final_balance = check_balance()
print("Balance : ", final_balance)

'''Q3 Create a function that accepts any number of values and returns:
sum
average
👉 Use *args.'''

def arguments(*args):
    if len(args) == 0:
        print("No values provided")
        return

    values = 0
    for num in args:
        values += num
    print("Sum :", values)
    print("Average :", values/len(args))

arguments(1,2,3,4,5)

'''Q4. User Profile Generator
Function accepts:
name
age
city
optional skills
👉 Return formatted profile using **kwargs.'''

def profile(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print("Profile Information :")
profile(name = "karthik",age = 20, city = "hosur")

'''Q5. Input Validation Function

Create a function that:

Accepts user input
Ensures input is numeric
Repeats until valid input is entered
👉 Must use loop + function together.'''

def validation():
    while True:
        num = input("Enter a Number: ")
        if num.isdigit():
            break
        else:
            print("Invalid Number.")

validation()






