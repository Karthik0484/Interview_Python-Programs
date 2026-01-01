''' LEVEL 3: REAL-WORLD SCENARIOS (FREQUENTLY ASKED)
Q1. Login System

Create a User class:
username
password
Method:
login(input_username, input_password)

📌 Tests: validation logic using OOP'''
class User:

    def __init__(self):
        self.username = "karthik"
        self.password = 12345678

    def login(self,uname,pwd):
        if self.username==uname and self.password==pwd:
            print("Login Successfull.")
        else:
            print("Invalid Login.")

user1 = User()
user1.login("karthik",12345678)

'''Q2. Online Order System

Create an Order class:
order_id
amount
Method:
apply_discount()
If amount > 5000 → 10% discount
📌 Tests: conditionals + constructor'''

class Order:

    def __init__(self,order_id,amount):
        self.order_id = order_id
        self.amount = amount

    def apply_discount(self):
        if self.amount > 5000:
            discount = self.amount * 0.1
            total = self.amount-discount
            print(f"Applied 10% Discount {total}")

        else:
            print("Not Eligible for discount.")

order1 = Order(21,8000)
order1.apply_discount()

'''Q3. Vehicle Speed Checker

Create a Vehicle class:
vehicle_type
speed

Method:
check_fine()

📌 Tests: real traffic rules logic'''

class Vehicle:

    def __init__(self,vehicle_type,speed):
        self.vehicle_type = vehicle_type.lower()
        self.speed = speed

    def check_fine(self):
        if self.vehicle_type =="bike" and self.speed > 80:
            print("Fine amount: 500")

        elif self.vehicle_type == "car" and self.speed > 100:
            print("Fine amount: 1000")

        elif self.vehicle_type == "truck" and self.speed > 120:
            print("Fine amount: 1500")

        else:
            print("No fine.")

v1 = Vehicle("bike",100)
v1.check_fine()

'''LEVEL 4: THINKING LIKE A DEVELOPER
Q4. College Management

Create:
Student class
Teacher class
Each has:
name
display_details()
📌 Tests: understanding of class design'''

class Student:

    def __init__(self,name,roll_no,dept):
        self.name = name
        self.roll_no = roll_no
        self.dept = dept

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.roll_no}")
        print(f"Dept: {self.dept}")

class Teacher:

    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.id}")
        print(f"Dept: {self.dept}")

s1 = Student("Karthik",44,"IT")
s1.display_details()

s2 = Teacher("Karthik",44,"IT")
s2.display_details()

'''Q5. Mobile Phone Class

Create a Mobile class:
brand
model
price
Create 3 mobiles and print the most expensive one.
📌 Tests: object comparison'''

class Mobile:

    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

m1 = Mobile("Vivo",1819,20000)
m2 = Mobile("Iphone",17,70000)
m3 = Mobile("Samsung","s20",40000)

mobiles = [m1,m2,m3]

expensive = mobiles[0]

for mobile in mobiles:
    if mobile.price > expensive.price:
        expensive = mobile

print(f"Most Expensive Mobile: {expensive.brand}"
      f"{expensive.model} - ₹{expensive.price}")

'''Q6. E-Commerce Product Filter

Create a Product class:
name
category
price
Filter products below a given price.
📌 Tests: real-world filtering logic'''

class Product:

    def __init__(self,name,category,price):
        self.name = name
        self.category = category
        self.price = price

p1 = Product("Laptop","Electronics",50000)
p2 = Product("Mouse","Electronics",1000)
p3 = Product("Dress","Fashion",10000)
p4 = Product("Sweater","Fashion",2000)

products = [p1,p2,p3,p4]

max_Price = 1000

print(f"Products Below: {max_Price}")
for prices in products:
    if prices.price < max_Price:
        print(f"{prices.name} ({prices.category} {prices.price})")


''' BONUS (VERY IMPRESSIVE IF YOU CAN DO)
Q7. Instance vs Class Attribute

Create a class where:
one attribute is shared by all objects
one attribute is unique per object

📌 Tests: deep understanding of OOP'''

class Dog:
    species = "German"

    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

d1 = Dog("Pug")
print(d1.species)
d1.display()

'''Q8. Constructor Validation
Create a class that does not allow negative values during object creation.
📌 Tests: validation inside __init__'''

class Validation:

    def __init__(self,name,price):

        if price < 0:
            raise ValueError("Price must be greater than 0.")
        self.name = name
        self.price=price

    def display(self):
        print(f"Product: {self.name}, Price: {self.price}")

v1 = Validation("Mobile",90000)
v1.display()



