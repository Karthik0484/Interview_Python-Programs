''' 🔹 LIST – Interview Questions
Q1. First Duplicate Finder (Very Common)

You are given a list of user IDs representing login attempts.
Return the first duplicate user ID encountered.
ids = [101, 203, 405, 203, 501, 101]
👉 Output: 203 '''


ids = [101, 203, 405, 203, 501, 101]

seen = set()

for num in ids:
    if num in seen:
        print("Duplicate Number: ",num)
        break
    seen.add(num)

''' Q2. Shopping Cart Cleanup
You are given a shopping cart list that may contain duplicate items.
Remove duplicates without changing the order.

cart = ["apple", "banana", "apple", "orange", "banana"]'''

cart = ["apple", "banana", "apple", "orange", "banana"]

original = []
for items in cart :
    if items in original:
        continue
    original.append(items)
print(original)

''' 
Q3. Second Largest Number
Find the second largest number in a list without using sort().

nums = [10, 45, 23, 45, 67, 67, 34] '''
nums = [10, 45, 23, 45, 67, 67, 34]

second_largest = 0
largest = 0

for i in nums:
    if i > largest :
        second_largest = largest
        largest = i
    if i > second_largest and i != largest:
            second_largest = largest

print(second_largest)

''' Q4. Split Even & Odd Numbers

Given a list of numbers, return two lists:
One with even numbers
One with odd numbers
Use only loops and conditions. '''

nums = [1,2,3,4,5,6,7,8]

even =[]
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even Numbers :",even)
print("Odd Numbers :",odd)

''' Q5. Frequency Counter
Count how many times each element appears in a list and store the result in a dictionary.
nums = [1, 2, 2, 3, 3, 3, 4]'''

nums = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for n in nums:
    if n in freq:
        freq[n] = freq[n] + 1
    else:
        freq[n] = 1
print(freq)






