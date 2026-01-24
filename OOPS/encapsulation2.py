'''Q1. Attendance System

Create a StudentAttendance class:
Attendance count is private
Attendance can only be increased by 1 per day
Cannot directly modify attendance'''
class Attendance:
    def __init__(self,name,roll_no):
        self.name = name
        self.__count = 0
        self.roll_no = roll_no

    def mark_attendance(self):
        self.__count += 1
        return "Attendance marked successfully."

    def get_attendance(self):
        return f"No of days present: {self.__count}"

a1 = Attendance('Karthik',44)
print(a1.mark_attendance())
print(a1.mark_attendance())
print(a1.mark_attendance())
print(a1.mark_attendance())
print(a1.get_attendance())

'''Q2. Shopping Wallet

Create a Wallet class:
Balance private
Add money with validation
Spend money only if balance is sufficient'''
class Wallet:

    def __init__(self,balance):
        self.__balance = balance

    def add_money(self,amount):
        if amount <= 0:
            return "Enter Valid Amount."
        else:
            self.__balance += amount
            return f"Money added: {amount}. Current balance: {self.__balance}"

    def spend_money(self, amount):
        if amount <= 0:
            return "Amount must be positive."

        if amount > self.__balance:
            return  "Insufficient Balance."

        self.__balance -= amount
        return f"Spent {amount}. Remaining balance: {self.__balance}"
    def get_balance(self):
        return f"Balance : {self.__balance}"

w1 = Wallet(1000)
print(w1.add_money(500))
print(w1.get_balance())

'''Q3. Hospital Patient Records

Create a Patient class:
Diagnosis is private
Only doctor method can update diagnosis
Public method to show basic details only'''

class Patient:

    def __init__(self,name,age):
        self.__diagnosis = None
        self.name=name
        self.age=age

    def update_diagnosis(self,diagnosis):
            self.__diagnosis = diagnosis
            return "Doctor Updated the diagnosis."

    def basic_details(self):
        print("Basic Details.")
        return f"Name: {self.name}, Age: {self.age}"

p1 = Patient('Adam',20)
print(p1.update_diagnosis('in progress'))
print(p1.basic_details())

'''Q4. Online Exam System

Create an Exam class:
Score is private
Score can be updated only once
Prevent multiple modifications'''

class Exam:
    def __init__(self,score):
        self.__score = score

    def update_score(self,new_score):
        if new_score < 0 or new_score > 100:
            return "Invalid score provided."

        self.__score = new_score
        return self.__score

    def get_marks(self):
        return self.__score

e1 = Exam(100)
print(e1.get_marks())
print(e1.update_score(68))

'''Q5. Library Fine System

Create a LibraryAccount class:

Fine amount is private
Fine calculated internally based on late days
User can only view total fine'''

class LibraryAccount:

    def __init__(self):
        self.__fine_amount = 0

    def calculate_fine(self,late_days):
        if late_days < 0:
            return "Enter Valid Late Days."

        self.__fine_amount = late_days*10
        return f"Fine Calculated Successfully."

    def get_fine(self):
        return f"Total Fine: {self.__fine_amount}"

l1 = LibraryAccount()
print(l1.calculate_fine(5))
print(l1.get_fine())

'''Q6. Mobile Phone Lock

Create a Mobile class:

Lock status is private
Phone unlocks only with correct PIN
Direct status change not allowed'''

class Mobile:

    def __init__(self):
        self.__lock_status = 'locked'
        self.__pin = 1234

    def unlock(self,pin):
        if self.__pin != pin :
            return "Enter Valid PIN."

        if self.__lock_status == 'unlocked':
            return "Mobile is already unlocked."

        self.__lock_status = 'unlocked'
        return f"Mobile phone: {self.__lock_status}"

    def get_status(self):
        return self.__lock_status

m1 = Mobile()
print(m1.unlock(1234))

'''Q7. Salary Slip Generator

Create a Salary class:
Basic salary private
HRA, bonus calculated internally
Final salary shown via getter'''
class Salary:

    def __init__(self,salary):
        if salary <= 0:
            raise ValueError("Basic salary must be positive.")
        self.__salary = salary

    def calculate_salary(self):
        HRA = self.__salary * 0.10
        Bonus = self.__salary * 0.20
        self.__final_salary= self.__salary+ HRA + Bonus

    def get_salary(self):
        return f"Final salary: {self.__final_salary}"

s1 = Salary(55000)
s1.calculate_salary()
print(s1.get_salary())

'''Q15. Secure Voting System

Create a Voter class:
Vote count private
Voter can vote only once
Prevent direct vote manipulation'''
class Voter:

    def __init__(self):
        self.__A = 0
        self.__B = 0
        self.__C = 0

    def vote(self,name):
        if name == 'A':
            self.__A += 1

        if name == 'B':
            self.__B += 1

        if name == 'C':
            self.__C += 1

        return "Enter Valid Candidate."

    def get_vote(self):
        return f"A: {self.__A} votes, B: {self.__B} votes, C: {self.__C} votes."

v1 = Voter()
v1.vote('A')
v1.vote('B')
v1.vote('A')
v1.vote('A')
print(v1.get_vote())













