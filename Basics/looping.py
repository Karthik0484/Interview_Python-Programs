''' 🔹 B. LOOPS – 5 INTERVIEW QUESTIONS
Q1. Shopping Cart Total

User keeps entering item prices.
Stop when user types done
Ignore negative values
Print total bill

👉 Use while, break, continue.'''

total = 0
while True:
    price= input("Enter Item Price(or type done to exit) :")

    if price.lower() == "done":
        break

    if not price.isdigit():
        print("Enter valid number.")
        continue

    price = int(price)
    if price < 0 :
        continue
    total += price

print("Your Bill is :", total)

''' Q2. Password Retry System

User gets 3 attempts to enter correct password.
Exit immediately on success
Lock account after 3 failures

👉 Use loop + conditional logic. '''

attempts = 0
correct_pwd = "karthi"
max_attempts = 3

while True:
    pwd = input("Enter Password: ")

    if pwd == correct_pwd:
        print("Login Success.")
        break

    else:
        attempts += 1
        print("Attempts left: ", max_attempts - attempts)

if attempts == max_attempts:
    print("Account Locked.")

''' Q3. Log File Analyzer

Given a list of server logs:
["INFO", "ERROR", "INFO", "WARNING", "ERROR"]

👉 Count how many ERROR messages occurred. '''

server_logs = ["INFO", "ERROR", "INFO", "WARNING", "ERROR"]
count = 0

for items in server_logs:
    if items == "ERROR":
        count += 1
        
print("No.of Error Message:",count)

''' Q4. Find First Duplicate

Given a list of numbers:
[4, 7, 2, 9, 7, 1]

👉 Print the first duplicate number and stop loop.  '''

num = [4,7,2,9,7,1]

seen = set()

for nums in num:
    if nums in seen:
        print("Duplicate number :", nums)
        break
    seen.add(nums)

''' 
Q5. Prime Numbers in Range

Input:
start
end
👉 Print all prime numbers in that range using loops. '''

start = int(input("Enter starting Number: "))
end = int(input("Enter last Number: "))

for num in range(start, end+1):
    if num < 1 :
        continue

    is_prime = True

    for i in range(2, int(num*0.5)+1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)










