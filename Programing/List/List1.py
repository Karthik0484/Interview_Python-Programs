'''1.Find sum of min number and max number without using in-built function'''

def sum(arr):
    highest = arr[0]
    lowest=arr[0]

    for i in range(1,len(arr)):
        if arr[i] > highest:
            highest=arr[i]
        elif arr[i]<lowest:
            lowest = arr[i]

    return f"Sum of Min and Max number:  {highest+lowest}"

print(sum([10,20,40,70,60]))

'''2.Program to check if the expression contains balanced brackets'''

s = input("Enter a expression containing brackets: ")
lst=[]

for i in s:
    if i == '{' or i=='[' or i=='(':
        lst.append(i)

    elif i== '}' and lst[-1]=='{':
        lst.pop()

    elif i== ']' and lst[-1] == '[':
        lst.pop()

    elif i==')' and lst[-1] =='(':
        lst.pop()
    else:
        break

if len(lst) == 0:
    print("Given expression contains balanced brackets.")

else:
    print("Given expression does not contains balanced brackets.")

'''3.Remove Duplicates
Given a list, remove duplicates without using set and maintain order.
Input: [1, 2, 2, 3, 4, 3, 5]
Output: [1, 2, 3, 4, 5]'''

lst=[1,2,2,3,4,3,5]
res=[]
seen=set()

for num in lst:
    if num not in seen:
        res.append(num)
        seen.add(num)

print(res)

'''4.Move All Zeros to End
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]'''

lst=[0, 1, 0, 3, 12]
pos=0

for i in range(len(lst)):
    if lst[i] != 0:
        lst[pos],lst[i]=lst[i],lst[pos]
        pos += 1

print(lst)

'''5.Program to insert element into a sorted list'''

lst=eval(input("Enter a list of elements: "))
n=int(input("Enter element to insert: "))

for i in range(len(lst)):
    if n<lst[i]:
        lst.insert(i,n)
        break

    if n>lst[-1]:
        lst.append(n)

print("After insertion: ",lst)


