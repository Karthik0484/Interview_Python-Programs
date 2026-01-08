'''🔹 METHOD OVERRIDING – Interview Favorites
Q1. Login System
Base class User → login()
Child class AdminUser → override login()
Admin should get extra access message.

Goal: Method overriding + access control'''
class User:

    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd

    def login(self,username,password):

        if self.uname == username and self.pwd==password:
            print(f"Login Successful Welcome {self.uname}")
            return True

        else:
            print("Invalid Credentials.")
            return False

class Admin(User):

    def __init__(self,uname,pwd,role):
        super().__init__(uname,pwd)
        self.role = role

    def valid_admin(self,):
        if self.role.lower() == 'admin':
            print( "Admin has Extra access.")
        else :
            print("You are not a Admin.")

u1 = Admin("Karthik",12345678,'admin')
if u1.login("Karthik",12345678):
    u1.valid_admin()

''' Q2. Vehicle Start System
Base class Vehicle → start()
Child classes Car, Bike, ElectricCar
Each overrides start() differently.
Goal: Behavior customization using overriding'''

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):

    def start(self):

        return f'Car has Started'

class Bike(Vehicle):

    def start(self):
        return f'Bike has started.'

class ElectricCar(Vehicle):

    def start(self):
        return f'Electric car has Started.'

c1 = [Car(),Bike(),ElectricCar()]

for i in c1:
    print(i.start())

'''Q3. Order Processing

Base class Order → calculate_bill()
Child class OnlineOrder → adds delivery charge
Child class StoreOrder → no delivery charge
Goal: Overriding business rules'''

class Order:

    def __init__(self,name):
        self.name = name
        self.items = []

    def add_item(self,price):
        self.items.append(price)

    def calculate_bill(self):
        total = sum(self.items)
        return total

class OnlineOrder(Order):

    def calculate_bill(self):
        total = sum(self.items)
        charges = total * 0.2
        return total + charges

class StoreOrder(Order):

    pass

o1 = OnlineOrder("Karthik")
o1.add_item(1000)
o1.add_item(2000)
o1.add_item(3000)
print(o1.calculate_bill())

o2 = StoreOrder("Aman")
o2.add_item(1000)
o2.add_item(2000)
o2.add_item(3000)
print(o2.calculate_bill())
















