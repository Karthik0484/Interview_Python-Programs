''' Q1. E-commerce Discount Engine

An e-commerce site gives:
20% discount if user is Premium
10% discount if order > ₹5000
Extra 5% if shopping day is Sunday

👉 Write a program to calculate final payable amount based on these rules. '''

order = 4000
has_premium = False
day = "sun"

# calculated discounts independently and applied the total discount at the end. This makes the logic scalable and easy to maintain.
discount = 0

if order > 5000:
    discount += 0.10

if has_premium:
    discount += 0.20

if day == "sun" :
    discount += 0.05

print("payable amount: ", order - (order * discount))

''' Q2. Login Access Control

User enters:

username
password
number of failed login attempts

Rules:

Lock account if attempts > 3
Allow login only if credentials are correct
Show different messages for wrong password vs locked account

👉 Implement using if-elif-else.'''

# Because login attempts are unknown in advance and should stop once either authentication succeeds or attempts exceed limit

correct_name = "Karthik"
correct_pwd = "12345678"



attempts = 0
max_attempts = 3

while attempts < max_attempts:
    name = input("Enter your Name: ")
    password = input("Enter your Password: ")

    if name == correct_name and password == correct_pwd:
        print("Login successful.")
        break
    else:
        attempts += 1
        print(f"Inavlid Credentials. Attempts Left: {max_attempts - attempts} ")

if attempts == max_attempts:
    print("Account locked due to multiple Failed Attempts.")

'''
Q3. Traffic Fine Calculator

Input:
vehicle type (bike, car, truck)
speed

Rules:
No fine if speed < limit
Fine differs per vehicle
Extra penalty if speed > 30 km/h above limit

👉 Print fine amount. '''

vehicle = input("Enter your Vehicle Type(bike/car/truck) : ").lower()
Speed = int(input("Enter Speed: "))

limit = 60

if Speed < limit :
    print("No fine ")

else:
    if vehicle == "bike":
        fine = 500
    elif vehicle == "car":
        fine = 1000
    elif vehicle == "truck":
        fine = 1500
    else:
        print("Invalid Vehicle Type.")
        exit()

    if Speed > limit+30:
        fine += 1000 # Added Extra penalty

    print("Fine amount: ", fine)

''' 

Q4. Student Result Analyzer

Input marks of 5 subjects.

Rules:

Fail if any subject < 35
Grade A: avg ≥ 85
Grade B: avg ≥ 70
Grade C: avg ≥ 50

👉 Print Pass/Fail + Grade. '''

sub1 = int(input("Enter mark of Subject1 : "))
sub2 = int(input("Enter mark of Subject2 : "))
sub3 = int(input("Enter mark of Subject3 : "))
sub4 = int(input("Enter mark of Subject4 : "))
sub5 = int(input("Enter mark of Subject5 : "))

avg = (sub1+sub2+sub3+sub4+sub5)/5
print(avg)

if sub1 < 35 or sub2 < 35 or sub3 < 35 or sub4 < 35 or sub5 < 35:
    print("Fail")

elif avg >= 85:
    print("pass, Grade A")

elif avg >= 70:
    print("pass, Grade B")

elif avg >= 50:
    print("pass, Grade C")

''' 
Q5. Banking Withdrawal Validation

Input:

balance
withdrawal amount
account type (salary / savings)

Rules:
Minimum balance differs
Withdrawal denied if balance rule breaks

👉 Print transaction status. '''

balance = int(input("Enter balance amount: "))
withdrawal = int(input("Enter withdrawal amount: "))
account_type = input("Enter account type (salary/savings): ").lower()

if account_type == "salary":
    min_balance = 0
elif account_type == "savings":
    min_balance = 1000
else:
    print("Invalid account type")
    exit()

if balance - withdrawal >= min_balance:
    print(f"Withdrawal successful. Amount withdrawn: {withdrawal}")
    print("Remaining balance:", balance - withdrawal)
else:
    print("Withdrawal denied. Minimum balance requirement not met.")

