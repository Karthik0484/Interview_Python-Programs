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



