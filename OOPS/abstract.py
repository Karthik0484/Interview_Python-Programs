'''🔹 ABSTRACTION – Very Important for Interviews
Q1. Payment Abstraction
Create an abstract class Payment with abstract method pay(amount).
Implement it in:
UPIPayment
CardPayment
Object should not be created for abstract class.

Goal: Hide implementation details'''

from abc import ABC,abstractmethod

from OOPS.intro import Employee


class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPIPayment(Payment):

    def pay(self,amount):
        print(f"Paid 💲{amount} using UPI.")

class CardPayment(Payment):

    def pay(self,amount):
        print(f"Paid 💲 {amount} using Card.")

u1 = UPIPayment()
u1.pay(1000)

c1=CardPayment()
c1.pay(2000)

'''Q2. Vehicle Control System
Abstract class Vehicle with abstract methods:
start()
stop()
Implement for Car and Bike.

Goal: Enforce rules using abstraction'''

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        return "Car Engine Starts."

    def stop(self):
        return "Car Engine Stopped."

class Bike(Vehicle):

    def start(self):
        return "Motor Bike Engine Starts."

    def stop(self):
        return "Motor Bike Engine Stopped."

c1 = Car()
print(c1.start())
print(c1.stop())

b1 = Bike()
print(b1.start())
print(b1.stop())

'''Q3. Employee Attendance System

Abstract class AttendanceSystem
Abstract method calculate_attendance()
Implemented by:
StudentAttendance
StaffAttendance
Goal: Abstract class as blueprint'''

class AttendanceSystem(ABC):

    def __init__(self,name,attendance):
        self.name = name
        self.attendance = attendance

    @abstractmethod
    def mark_attendance(self):
        pass

    @abstractmethod
    def show_attendance(self):
        pass

class StudentAttendance(AttendanceSystem):

    def __init__(self,name,attendance):
        super().__init__(name,attendance)

    def mark_attendance(self):
        self.attendance += 1

    def show_attendance(self):
        return f"Student {self.name} is present {self.attendance} days."

class EmployeeAttendance(AttendanceSystem):

    def __init__(self,name,attendance):
        super().__init__(name,attendance)

    def mark_attendance(self):
        self.attendance += 1

    def show_attendance(self):
        return f"Employee {self.name} is present {self.attendance} days."

s1 = StudentAttendance("Karthik",0)
s1.mark_attendance()
s1.mark_attendance()
print(s1.show_attendance())

s1 = EmployeeAttendance("Smith",0)
s1.mark_attendance()
s1.mark_attendance()
s1.mark_attendance()
s1.mark_attendance()
print(s1.show_attendance())




