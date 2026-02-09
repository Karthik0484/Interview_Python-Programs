'''🟢 11. Move Zeros to End
🧠 Scenario
A data cleaning tool wants all zeros moved to the end.

❓ Problem
Move all zeros to the end while keeping order.'''
from Basics.lists import second_largest

arr = [0, 1, 0, 3, 12]
pos =0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1

while pos < len(arr):
    arr[pos] = 0
    pos+=1

print(arr)

'''🟢 12. Frequency Count
🧠 Scenario
A voting system counts how many times each candidate appears.

❓ Problem
Count frequency of each element.'''
arr = [1, 2, 2, 3, 1]

dict ={}

for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)

'''🟢 13. First Non-Repeating Element
🧠 Scenario
A queue system wants the first unique ticket number.

❓ Problem
Find the first non-repeating element. '''
arr = [4, 5, 1, 2, 1, 1]
dict = {}
non_repeating = 0

for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i] = 1

for key,values in dict.items():
    if values == 1:
        non_repeating = key
        break

print(non_repeating)

'''🟢 14. Second Largest Element
🧠 Scenario
A leaderboard needs the runner-up score.

❓ Problem
Find the second largest element.'''
def second_lar(arr):
    if len(arr) < 2:
        return "Elements not enough."

    first = second = float("-inf")

    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]

        elif i > second and i!= first:
            second = i

    return second

print(second_lar([10, 5, 20, 8]))

'''🟢 15. Missing Number (1 to N)
🧠 Scenario
A roll number list has one missing entry.

❓ Problem
Find the missing number from 1 to N.

Input:
arr = [1, 2, 4, 5]

Output:
3'''

def missing_number(arr):
    n= len(arr)+1
    actual_sum = n*(n+1)//2
    total_sum = sum(arr)
    missing_num = actual_sum-total_sum
    return missing_num

print(missing_number([1, 2, 4, 5]))

'''🟢 16. Subarray Sum
🧠 Scenario
A finance system checks if expenses add up to a target.

❓ Problem
Check if any subarray has sum = K.'''
# Brute force Approach
arr = [1, 4, 20, 3, 10, 5]
K = 33
n = len(arr)

found = False

for i in range(n):
    current_sum = 0
    for j in range(i,n):
        current_sum += arr[j]
        if current_sum == K:
            found = True
            break

if found:
    print("Yes")

else:
    print("No")

# Optimized Approach – Sliding Window

arr = [1, 4, 20, 3, 10, 5]
K = 33

start = 0
current_sum = 0

for end in range(len(arr)):
    current_sum += arr[end]

    while current_sum > K and start < end:
        current_sum -= arr[start]
        start += 1

    if current_sum == K:
        print("Yes.")
        break

else:
    print("No.")

'''🟢 17. Rotate Array
🧠 Scenario
A log system rotates data daily.

❓ Problem
Rotate array left by K positions.

Input:
arr = 
K = 2
Output:
[3, 4, 5, 1, 2]'''

def rotate(arr,K):
    n = len(arr)
    K=K%n

    first=arr[:K]
    second = arr[K:]

    final=second + first

    return final

print(rotate([1,2,3,4,5],2))

# Or

def rotate_array(arr,K):
    return arr[K:] +arr[:K]

print(rotate_array([6,7,8,9,10],2))

# Or Rotate Array using REVERSAL

def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end-=1

def rotate(arr,K):
    n = len(arr)
    K = K%n

    reverse(arr,0,K-1)
    reverse(arr,K,n-1)
    reverse(arr,0,n-1)

    return arr

print(rotate([10,20,30,40,50],3))


'''🟢 18. Insert Element at Index
🧠 Scenario
A record system inserts a value at a specific position.

❓ Problem
Insert an element at given index.

Input: arr = [1, 2, 4, 5], index = 2, value = 3

Output: [1, 2, 3, 4, 5]'''

def inserting(arr,index,value):
    arr.insert(index,value)
    return arr

print(inserting([1,2,4,5],2,3))


# No Insert

def insert_ele(arr,index,value):
     arr.append(0) # increase size

     for i in range(len(arr)-1,index,-1):
         arr[i] = arr[i-1]

     arr[index] = value

     return arr

print(insert_ele([10,20,40,50],2,30))

'''🟢 19. Delete Element at Index
🧠 Scenario
An admin removes invalid data.

❓ Problem
Delete element at a specific index.

Input: arr = [10, 20, 30, 40], index = 1

Output: [10, 30, 40]'''

def remove(arr,index):
    arr.pop(index)
    return arr

print(remove([1,2,3,4,5],2))

'''🟢 20. Handle Edge Cases
🧠 Scenario
Your system should never crash.

❓ Problem
Handle these cases properly:

Empty array
Single element array

Input:arr = []
Output:Array is empty'''

def handle_edge_case(arr):
    n = len(arr)

    if n == 0:
        return f"Array is empty."

    elif n==1:
        return "Array has 1 element."

    else:
        return f"Array has {n} elements."

print(handle_edge_case([1]))










