'''🟢 LEVEL 1: CLASS, OBJECT, CONSTRUCTOR (VERY COMMON)

Q1. Student Management
Create a Student class with:
name
roll number
marks
Create multiple student objects and display their details.'''

class Student:
    def __init__(self,name,marks,roll_no):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no

    def display(self):
        print(f"Name:{self.name}, Roll_No:{self.roll_no}, Marks: {self.marks}")

stu1 = Student("Karthik",90,44)
stu1.display()

stu2 = Student("Aravind",85,"06")
stu2.display()

'''Q2. Bank Account System
Create a BankAccount class with:
account_holder
balance

Methods:
deposit(amount)
withdraw(amount)
display_balance()'''

class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        print(f"Amount Deposited: {amount}")
        self.balance += amount
        return self.balance

    def withdraw(self,amount):

        if amount > self.balance:
            print("Insufficient Balance.")
        else:
            print(f"Amount Withdrawn: {amount}")
            self.balance -= amount
            return self.balance


    def display(self):
        print(f"Remaining balance: {self.balance}")
        return self.balance

b1 = BankAccount("Karthik",1000)
b1.deposit(1000)
b1.display()

'''Q3. Employee Salary Calculator
Create an Employee class:
name
basic_salary
Method:
calculate_salary()
Add 20% HRA
Add 10% bonus

📌 Tests: business logic inside class'''

class Employee:

    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        if self.basic_salary <= 0:
            print("Invalid salary")
        else:
            salary = self.basic_salary
            hra = salary * 0.2
            bonus = salary * 0.1
            total = salary + hra + bonus
            print(f"Employee: {self.name}, Total Salary: {total}")

emp1 = Employee("Karthik",60000)
emp1.calculate_salary()

'''
🟡 LEVEL 2: MULTIPLE OBJECTS + METHODS
Q4. Library Book System
Create a Book class:
title
author
available (True/False)

Methods:
borrow_book()
return_book()
Create multiple books and simulate borrowing.'''

class Book:

    def __init__(self,title,author,available):
        self.title = title
        self.author = author
        self.available = True

    def borrow_books(self):
        if self.available:
            self.available = False
            print(f"You Borrowed {self.title} by {self.author} ")
        else:
            print("Book is already Borrowed.")

    def return_book(self):
        self.available = True
        print(f"You Returned {self.title}")

b1 = Book("Atomic Habits","James Clear",True)
b1.borrow_books()
b1.return_book()

'''Q5. Shopping Cart

Create a Product class:
name
price
Create multiple products and calculate total cart price.'''

class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

class Cart:

    def __init__(self):
        self.products = []

    def add_items(self,product):
        self.products.append(product)

    def total_bill(self):
        total = 0
        for prices in self.products:
            total += prices.price
        print(f"Total Prices is : {total}")

b1 = Product("Laptop",50000)
b2 = Product("Mouse",5000)

c1 = Cart()
c1.add_items(b1)
c1.add_items(b2)

c1.total_bill()

'''Q6. Attendance System

Create a Student class:
name
attendance_count
Methods:
mark_attendance()
show_attendance()'''

class Attendance:

    def __init__(self,name):
        self.name = name
        self.attendance_count = 0

    def mark_attendance(self):
        self.attendance_count += 1

    def show_attendnace(self):
        print(f"{self.name} is {self.attendance_count} days present.")

a1 = Attendance("Karthik",)
a1.mark_attendance()
a1.mark_attendance()

a1.show_attendnace()












