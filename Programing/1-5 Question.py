'''1️⃣ Reverse a String (Without Using Built-in Reverse)
Problem
Given a string, reverse it without using any built-in reverse function.'''

# 1️⃣ Python Slicing ⏱ Time Complexity  O(n) → Python traverses the string once
                  # 🧠 Space Complexity O(n) → new reversed string is created
a='programming'
print(a[::-1])

# 2️⃣ Prepending Characters ⏱ Time Complexity O(n²)  🧠 Space Complexity O(n) (final string)
rev =''
for ch in a:
    rev = ch +rev
print(rev)

# 3️⃣ Using List + Join (Recommended) ⏱ Time Complexity O(n) ✅ 🧠 Space Complexity O(n)
chars =[]

for ch in a:
    chars.append(ch)

chars.reverse()
reve =''.join(chars)
print(reve)

# 4️⃣ Two-Pointer Swap (Array In-Place) ⏱ Time Complexity O(n) ✅ 🧠 Space Complexity O(1) (excluding output)
chars = list(a)
l,r = 0, len(chars)-1

while l<r:
    chars[l], chars[r] = chars[r],chars[l]
    l += 1
    r -= 1

reverse = ''.join(chars)
print(reverse)

'''2️⃣ Check if a Number is a Palindrome
Problem
Given an integer, check whether it reads the same forward and backward.'''

# 🧠 APPROACH 1: Reverse the Number ⏱ Time Complexity O(d) (d = number of digits) 🧠 Space Complexity O(1)

a=1221
original = a
rev = 0

while a >0:
    digit = a%10
    rev = rev*10 + digit
    a =a//10

if rev == original:
    print("It's Palindrome.")

else:
    print("It's not a palindrome.")

# 🧠 APPROACH 2: Reverse HALF of the Number(ADVANCED / OPTIMAL) ⏱ Time Complexity O(d / 2) ≈ O(d) 🧠 Space Complexity O(1)

def isPalindrome(n: int):
    if n < 0 or (n%10==0 and n!=0):
        return False

    revers=0
    while n>revers:
        revers = revers*10 + n%10
        n = n//10

    return revers == n or n == revers // 10

print(isPalindrome(101))

'''3️⃣ Find the Second Largest Element in an Array
Problem
Given an array of integers, find the second largest unique element.'''

a = [20,20,10,30,40,50]

def sec_largest(arr):
    largest = second_largest = float("-inf")

    for i in a:
        if i > largest:
            second_largest = largest
            largest=i

        elif i>second_largest and i!= largest:
            second_largest = i

    if second_largest==float('-inf'):
        print("No second largest element.")
    else:
        return second_largest

print(sec_largest(a))

'''4️⃣ Count Frequency of Characters in a String 
Problem
Given a string, count how many times each character appears.'''

# ⏱ Time Complexity O(n) 🧠 Space Complexity O(n)

s='Karthik'.lower()
freq={}

for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

'''5️⃣ Find Missing Number in an Array (1 to N)
Problem
An array contains numbers from 1 to N with one number missing. Find the missing number.'''
# ⏱ Time Complexity O(n) 🧠 Space Complexity O(1)
num = [1, 2, 3, 5]

def missing_number(num):
    n = max(num)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(num)
    missing_num = expected_sum-actual_sum

    return missing_num

print(missing_number(num))








