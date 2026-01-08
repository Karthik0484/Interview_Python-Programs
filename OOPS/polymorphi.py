'''🔹 POLYMORPHISM – Real-World Interview Questions
Q1. Notification System

Create a base class Notification.
Child classes:
EmailNotification
SMSNotification
PushNotification
Each sends message differently using the same method name.

Goal: Polymorphism in messaging systems'''
class Notification:

    def notify(self):
        return f"This is  Notification."

class EmailNotification(Notification):

    def notify(self):
        return  "This is Email Notification "

class SMSNotification(Notification):

    def notify(self):
        return "This is SMS Notification."

class PushNotification(Notification):

    def notify(self):
        return "This is Push Notification."

# Polymorphism in action
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    print(n.notify())

'''Q2. Payment Gateway

Create base class Payment.
Child classes:
CreditCard
UPI
NetBanking
Each processes payment differently.

Goal: Polymorphism + real-world fintech use'''

class Payment:

    def paid(self):
        return "Paying the Bill."

class Creditcard(Payment):

    def paid(self):
        return "Paid the bill using Credit Card."

class UPI(Payment):

     def paid(self):
         return "Paid the bill using UPI."

class NetBanking(Payment):

    def paid(self):
        return "Paid the bill using NetBanking."

Payments = [Creditcard(),UPI(),NetBanking()]

for pay in Payments:
    print(pay.paid())

'''Q3. Shape Area Calculator

Create base class Shape with area() method.
Child classes Circle, Rectangle, Triangle.

Call area() using a parent reference.
Goal: Runtime polymorphism'''

class Shape:

    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return f"Area of circle :{3.14 * self.radius * self.radius}"

class Rectangle(Shape):

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return f"Area of Rectangle :{self.length * self.breadth}"

class Triangle(Shape):

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return f"Area of Triangle : {0.5 * self.length*self.breadth}"

c1 = Circle(2)
print(c1.area())

r1 = Rectangle(10,20)
print(r1.area())

t1 = Triangle(10,20)
print(t1.area())