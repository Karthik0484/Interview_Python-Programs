'''1.Create a list of even numbers from 2 to 2000.
get two numbers, x and y, which are positions (1-based) in this list.
Calculate the sum of the numbers from position x to position y (inclusive).
Print the sum.'''

def solution():
    nums =[]
    x ,y = map(int, input("Enter starting and ending Index: ").split())
    sum = 0
    for i in range(2 ,2001 ,2):
        nums.append(i)

    extract = nums[ x -1:y]

    for i in range(len(extract)):
        sum += extract[i]

    print(sum)
# Call the function
solution()

'''2.Given an array of integers, calculate and return the sum of its elements. 
Input Format:
The first line contains an integer , denoting the size of the array.
The second line contains space-separated integers representing the array's elements'''

def solution(n):
    nums = list(map(int, input("Enter Array Elements: ").split()))
    arr_sum = 0
    for i in range(len(nums)):
        arr_sum += nums[i]

    print(arr_sum)

solution( n= int(input("Enter a number ")))