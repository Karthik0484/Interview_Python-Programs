'''🟢 1. Array Traversal
🧠 Scenario
You are given daily sales data of a shop stored in an array. You need to display each day’s sales.

❓ Problem
Given an array of integers, print all elements one by one.'''
arr = [10, 20, 30, 40]

for ele in arr:
    print(ele)

'''🟢 2. Sum of Elements
🧠 Scenario
A teacher wants to calculate the total marks scored by a student across subjects.

❓ Problem
Find the sum of all elements in the array.'''
arr = [50, 60, 70, 80]
total = 0

for ele in arr:
    total += ele
print(total)

'''🟢 3. Largest & Smallest Element
🧠 Scenario
An HR system stores salaries of employees. You must find the highest and lowest salary.

❓ Problem
Find the maximum and minimum element in the array.'''
arr = [25000, 40000, 18000, 60000, 32000]
print(max(arr))
print(min(arr))

# or

max = arr[0]
min =arr[0]

for ele in arr:
    if ele > max:
        max = ele
    if ele < min :
        min = ele
print(f"Max element: {max}, Min element : {min}")


'''🟢 4. Count Even and Odd Numbers
🧠 Scenario
An exam system wants to count how many even roll numbers and odd roll numbers are present.

❓ Problem
Count even and odd numbers in an array.'''
arr = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0

for ele in arr:
    if ele%2 == 0:
        even += 1
    else:
        odd += 1
print(f"Even: {even}, Odd: {odd}")

'''🟢 5. Check if Array is Sorted
🧠 Scenario
Before applying binary search, you must verify whether the data is sorted.

❓ Problem
Check if the array is sorted in ascending order.'''

def is_sorted(arr):
    if len (arr) <1:
        return "Array is sorted."

    prev=arr[0]
    for ele in arr[1:]:
        if ele < prev:
            return "Array is not sorted."
        prev = ele
    return "Array is Sorted."

print(is_sorted([10,20,30,40]))
print(is_sorted([50,20,30,40]))

'''🟢 6. Linear Search (Find Index)
🧠 Scenario
A student searches for their roll number in a list.

❓ Problem
Find the index of a given element using linear search.

Output:
Index = 2'''

def linear_search(array,target):

    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(linear_search([5, 10, 15, 20],15))

'''🟢 7. Find All Occurrences
🧠 Scenario
An analytics system wants to know all positions where a particular value appears.

❓ Problem
Print all indices where a given element occurs.'''

arr =[1, 2, 3, 2, 4, 2]
key = 2
Indices = []

for i in range(len(arr)):
    if arr[i] == key:
        Indices.append(i)

print(Indices)

'''🟢 8. Binary Search (Sorted Array)
🧠 Scenario
A fast lookup system uses binary search to find records.

❓ Problem
Search an element using binary search.

Input:
arr = [10, 20, 30, 40, 50]
key = 40

Output:
Element found at index 3'''

def binary_search(arr,key):

    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1
    return -1

print(binary_search([1, 2, 3, 2, 4, 2],2))

'''🟢 9. Reverse an Array
🧠 Scenario
A system needs to display data in reverse chronological order.

❓ Problem
Reverse the array.

Input:
arr = 
Output:
[4, 3, 2, 1]'''

def reverse(arr):
    low = 0
    high = len(arr)-1

    while low < high:
        arr[low],arr[high] = arr[high],arr[low]
        low += 1
        high-=1

    return arr

print(reverse([1,2,3,4]))

''' 10. Reverse Array In-Place
🧠 Scenario
Memory is limited. You must reverse the array without extra space.

❓ Problem
Reverse array without using another array.

Input:
arr = [10, 20, 30]

Output:
[30, 20, 10]'''

def reverse(arr):
    low = 0
    high = len(arr)-1

    while low < high:
        arr[low],arr[high] = arr[high],arr[low]
        low += 1
        high-=1

    return arr

print(reverse([1,2,3,4]))