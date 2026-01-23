'''Q1. Bank Account Security

Create a BankAccount class where:

Balance is private
Balance cannot be set directly
Deposit amount must be positive
Withdrawal should not exceed balance
'''

class BankAccount:

    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount < 0:
            return "Invalid Amount."
        else:
            self.__balance += amount
            return self.__balance

    def withdraw(self,amount):
        if amount <0 :
            print( "Withdrawl Amount Must be Positive.")

        elif amount > self.__balance:
            print( "Insufficient Balance")

        else:
            self.__balance -= amount
            print( f"Withdraw Success {amount}.")

B1 = BankAccount(1000)
print(B1.get_balance())
print(B1.deposit(7000))
print(B1.withdraw(1000))
print(B1.get_balance())
print(B1.deposit(-500))

'''Q2. Student Marks Validation

Create a Student class:
Marks should be private
Marks must be between 0 and 100
Use getter and setter to update marks safely'''

class Student:

    def __init__(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if marks < 0 or marks > 100:
            print(f"Invalid Marks provided {marks}")

        else:
            self.__marks = marks
            return self.__marks

s1 = Student(100)
print(s1.get_marks())
s1.set_marks(20)
print(s1.get_marks())

'''Q3. Employee Salary Protection

Create an Employee class:
Salary is private
Salary can be increased but not decreased
Invalid salary update should be rejected'''

class Employee:

    def __init__(self,salary):
        self.__salary = salary

    def increase_salary(self,increment):
        if increment <0:
            print("Invalid Salary update.")
            return

        else:
            self.__salary += increment
            return self.__salary

    def get_salary(self):
        return self.__salary

e1 = Employee(10000)
print(e1.increase_salary(50000))
print(e1.get_salary())

'''Q4. ATM PIN Security
Create an ATMAccount class:

PIN must be private
User can change PIN only if old PIN matches
Direct access to PIN is not allowed'''

class ATMAccount:

    def __init__(self):
        self.__oldpin = 9876

    def change_pin(self,old_pin,new_pin):
        if self.__oldpin != old_pin:
            return "Invalid old PIN."

        if not (1000 <= new_pin <= 9999):
            return "PIN must be 4 digits."


        if new_pin == old_pin:
            return "New PIN cannot be same as old PIN."

        self.__old_pin=new_pin
        return "PIN updated successfully."

a1 = ATMAccount()
print(a1.change_pin(9876,8932))

'''Q5. Product Price Control

Create a Product class:
Price is private
Price cannot be negative
Apply discount only through a method'''

class Product:
    def __init__(self,price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price=price

    def apply_discount(self,percent):
        if percent <= 0 or percent>50:
            print("Invalid discount percentage.")
            return

        else:
            discount = self.__price * percent/ 100
            self.__price -= discount
            return f"Discount applied: {discount}, Final Price: {self.__price}"

    def get_price(self):
        return self.__price

p1 = Product(1000)
print(p1.apply_discount(1))
print(p1.get_price())

'''Q6. Login System with Encapsulation

Create a User class:
Username public
Password private
Login method validates credentials'''

class User:
    def __init__(self,name,pwd):
        self.name = name
        self.__pwd = pwd

    def login(self,name,pwd):
        if self.name==name and self.__pwd==pwd:
            print("Login Successful.")

        else:
            print("Invalid Credentials.")

u1 = User('Karthik',987654321)
u1.login('Karthik',987654321)





