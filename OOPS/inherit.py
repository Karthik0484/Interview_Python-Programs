'''Q1. Employee Hierarchy (Very Common)

Create a base class Employee with:
name
emp_id
Create a child class Developer with:
programming_language

Task:
Display full employee details using inheritance.'''

class Employee:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"{self.name} {self.emp_id} is Working.")

class Developer(Employee):

    def __init__(self,name,emp_id,programming):
        super().__init__(name,emp_id)
        self.programming = programming

    def carrer(self):
        print(f"{self.name} is {self.programming} Developer.")

d1 = Developer("Karthik",44,"Python")
d1.display()
d1.carrer()

'''Q2. Bank Account System

Create:
Account class → account_number, balance
SavingsAccount → interest_rate

Task:
Add interest to balance
Show updated balance
(Tests: super(), real-world logic)'''

class Account:
    def __init__(self,account_num,balance):
        self.account_num = account_num
        self.balance = balance

    def details(self):
        print(f"Account Details: {self.account_num}, {self.balance}")

class Savings(Account):

    def __init__(self,interest_rate,account_num,balance):
        super().__init__(account_num,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * (self.interest_rate/100)
        return self.balance

s1=Savings(10,5044,1000)
s1.details()
print(s1.add_interest())

'''Q3. Vehicle Speed Check
Create:
Vehicle → speed
Car → brand
Bike → engine_cc

Task:
If speed exceeds limit, print fine
Different limits for car and bike'''

class Vehicle:

    def __init__(self,speed):
        self.speed = speed

    def show(self):
        print(f"Speed : {self.speed}")

class Car(Vehicle):

    def __init__(self,brand,speed):
        super().__init__(speed)
        self.brand = brand

    def calculate_fine(self):
        limit = 100
        if self.speed > limit:
            print("Fine Amount: Rs.1000")
        else:
            print("No fine.")

class Bike(Vehicle):

    def __init__(self,engine_cc,speed):
        super().__init__(speed)
        self.engine_cc = engine_cc

    def calculate_fine(self):
        limit = 80
        if self.speed > limit:
            print("Fine Amount: Rs.500")

        else:
            print("No fine.")

c1 = Car("BMW",200)
c1.calculate_fine()

b1=Bike(150,20)
b1.calculate_fine()

'''Q4. Online Shopping Discount
Create:
Product → name, price
ElectronicsProduct → warranty_years

Task:
Apply 10% discount if price > 50,000
Print final price'''

class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} is Rs. {self.price}")

class Electronics(Product):

    def __init__(self,name,price,warranty_years):
        super().__init__(name,price)
        self.warranty_years = warranty_years

    def final_bill(self,discount_limit = 50000):
        if self.price > discount_limit:
            discount = self.price*0.10
            self.price -= discount
            print("Final Bill: ",self.price)
        else:
            print(f"Final Bill: {self.price} Warranty years: {self.warranty_years}")

p1 = Electronics("Laptop",80000,5)
p1.final_bill()
p1.display()

'''Q5. Login System (Inheritance + Validation)
Create:
User → username, password
AdminUser → admin_level

Task:
Validate login
Admin should get extra access message'''

class User:

    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd

    def validate_login(self,username,password):
        if self.uname == username and self.pwd == password:
            print(f"Login Successful {self.uname}")
            return True

        else:
            print("Invalid Credentials.")
            return False

class Admin(User):
    def __init__(self,uname,pwd,role):
        super().__init__(uname,pwd)
        self.role = role

    def valid_admin(self):
        if self.role.lower() == 'admin':
            print("Admin Has extra access.")
        else:
            print("You are not a Admin.")

a1 = Admin("Karthik",12345678,'Admin')
if a1.validate_login("Karthik",12345678):
    a1.valid_admin()

'''
Q6. College Management

Create:
Person → name, age
Student → roll_no, department
Teacher → subject

Task:
Display details for both student and teacher objects
(Tests: hierarchical inheritance)'''

class Person:

    def __init__(self,name,age):

        self.name = name
        self.age = age

class Student(Person):

    def __init__(self,name,age,roll_no,dept):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.dept = dept

    def display(self):
        print(f"Student Details: Name: {self.name}, Age: {self.age}, Roll: {self.roll_no}, Dept: {self.dept}")

class Teacher(Person):

    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def display_details(self):
        print(f"{self.name} is Handling {self.subject}")

stu = Student("Karthik",20,44,"IT")
stu.display()

t1 = Teacher("Ramya",35,"Python")
t1.display_details()

'''Q7. Salary Calculation
Create:
Employee → basic_salary
Manager → bonus_percentage

Task:
Calculate total salary using inheritance'''

class Employee:

    def __init__(self,name,emp_id,sal):
        self.name = name
        self.emp_id = emp_id
        self.sal = sal

class Manager(Employee):

    def __init__(self,name,emp_id,sal,bonus):
        super().__init__(name,emp_id,sal)
        self.bonus = bonus

    def salary(self):
        if self.bonus < 0:
            raise ValueError("Invalid bonus")

        else:
            total = self.sal * (self.bonus / 100)
            self.sal += total
            return self.sal

m1 = Manager("Karthik",100,50000,20)
print(m1.salary())





