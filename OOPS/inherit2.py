''' Q8. Method Overriding (Very Important)

Create:
Notification → send_message()
EmailNotification → override send_message()
SMSNotification → override send_message()

Task:
Call method using parent reference '''

class Notification:

    def send_message(self):
        print("Hi, How are you ?")

class EmailNotification(Notification):

    def send_message(self):
        print("This is Email Notification.")

class SMSNotification(Notification):

    def send_message(self):
        print("This is SMS Notification.")

e1 = EmailNotification()
e1.send_message()

s1 = SMSNotification()
s1.send_message()

'''Q9. Attendance System

Create:
Student → total_classes
Attendance → attended_classes

Task:
Calculate attendance percentage
If < 75%, print warning'''

class Student:

    def __init__(self,name,roll_no,total_class):
        self.name = name
        self.roll_no = roll_no
        self.total_class = total_class

class Attendance(Student):

    def __init__(self,name,roll_no,total_class,attended_classes):

        super().__init__(name, roll_no,total_class)
        self.attended_classes = attended_classes

    def calculate_attendance(self):
        percentage = (self.attended_classes / self.total_class)*100
        if percentage < 75:
            print(f"Attendance Shortage less tha 75% : {percentage}%")

        else:
            print(f"Attendance Percentage: {percentage}")

a1 = Attendance("Karthik",44,80,76)
a1.calculate_attendance()

'''Q10. Multiple Inheritance (Tricky)

Create:
Student → name
Employee → emp_id
TeachingAssistant inherits both

Task:
Display name and employee ID
Use correct constructor calls'''

class Student:

    def __init__(self,name):
        self.name = name

class Employee:

    def __init__(self,emp_id):
        self.emp_id = emp_id

class Teaching_Assistant(Student,Employee):

    def __init__(self,name,emp_id,sal):
        Student.__init__(self,name)
        Employee.__init__(self,emp_id)
        self.sal = sal

    def details(self):
        a = self.name,self.emp_id,self.sal
        return a

t1 = Teaching_Assistant("Karthik",44,50000)
print(t1.details())

'''Q11. E-Commerce Order System
Create:
Order → order_id, amount
OnlineOrder → delivery_charge

Task:
Calculate final payable amount'''

class Order:

    def __init__(self,order_id,amount):
        self.order_id = order_id
        self.amount = amount

class OnlineOrder(Order):

    def __init__(self,order_id,amount):
        super().__init__(order_id,amount)
        self.delivery_charge = 0.1

    def final_bill(self):
        return self.amount + (self.amount* self.delivery_charge)

o1 = OnlineOrder(1012,600)
print(o1.final_bill())

'''Q12. Library Management
Create:
Book → title, author
IssuedBook → issued_to, issued_days

Task:
If issued_days > 7, calculate fine'''

class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

class IssuedBook(Book):

    def __init__(self,title,author,issued_to,issued_days):
        super().__init__(title,author)
        self.issued_to = issued_to
        self.issued_days = issued_days

    def validity(self):
        fine = 10
        if self.issued_days > 7:
            expired = self.issued_days-7
            print(f"Validity Expired before {expired} days")
            return expired * fine
        else:
            print(f"validity exists for {7-self.issued_days} days")
            return  7-self.issued_days

i1 = IssuedBook("Atomic Habits","James Clear","Karthik",15)
print(i1.validity())

'''Q13. Shape Area Calculator
Create:
Shape → area()
Rectangle → length, breadth
Circle → radius

Task:
Override area() for each shape'''

class Shape:
     def area(self):
         pass

class Rectangle(Shape):

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return {'Area of Rectangle': self.length * self.breadth}

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return {'Area of Circle:', 3.14*self.radius * self.radius}

shapes = [Rectangle(5,5), Circle(3)]

for shape in shapes:
    print("Area : ",shape.area())

'''Q14. Company Role System
Create:
Employee → name
HR → handle_recruitment()
Developer → write_code()

Task:
Call correct role behavior using objects'''

class Employee:

    def __init__(self,name):
        self.name = name

class HR(Employee):

    def handle_recruitment(self):
        print(f"{self.name} handles Recruitment.")

class Developer(Employee):

    def write_code(self):
        print(f"{self.name} writes the code.")

hr1 = HR("Karthik")
hr1.handle_recruitment()

d1 = Developer("Karthik")
d1.write_code()

'''Q15. Inheritance + Exception Handling (Advanced)
Create:
Account → balance
WithdrawAccount → withdraw(amount)
Task:
Raise exception if withdrawal > balance'''

class Account:

    def __init__(self,balance):
        self.balance = balance

class WithdrawAmount(Account):

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance.")
        else:
            self.balance -= amount
            return self.balance

try:
    w1 = WithdrawAmount(1000)
    print(w1.withdraw(100))

except ValueError as e:
    print(e)








