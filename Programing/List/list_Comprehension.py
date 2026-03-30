'''1.Program to print squares of lst'''

lst=[3,5,7,8,10]

''' Traditional Approach
res=[]

for num in lst:
    res.append(num**2)

print("Original List: ",lst)
print("Squared List: ",res)'''

'''Using List comprehension'''

res =[num**2 for num in lst]
print("Original List: ",lst)
print("Squares using List comprehension:",res)

'''2.Printing squares of a number if it is even else double it.'''

lst=[3,5,7,8,10]

'''Traditional Approach
res=[]
for num in lst:
    if num%2 == 0:
        res.append(num**2)
    else:
        res.append(num+num)

print(res)'''

'''Using List Comprehension'''

res=[num**2 if num%2==0 else num+num for num in lst]
print("Using List comprehension: ",res)

'''3.Program to count number of vowels in a string'''
s="India is my country"
vowels="aeiouAEIOU"
count=[]

'''Traditional Approach

for char in s:
    if char in vowels:
        count.append(char)

print("No.of Vowels in a string:",len(count))'''

'''Using List comprehension

res=[count.append(char) for char in s if char in vowels]
print(len(count)) 

# Single line Code
print(len([i for i in input() if i in vowels])) '''

'''4.Program to find pairs from 2 list'''

lst1=[2,4,3]
lst2=[5,4,2,1]
res=[]

'''Traditional Approach
for i in lst1:
    for j in lst2:
        if i!=j:
            res.append((i,j))

print("Paired two list: ",res) '''

'''Using list comprehension'''
pairs=[(i,j) for i in lst1 for j in lst2 if i!=j]
print(pairs)

'''5.Program to print number and it's cube till N
n=int(input("Enter n: "))
cubes=[]

for i in range(1,n+1):
    cubes.append((i,i**3))

print(cubes)'''

'''Using List Comprehension'''
print([(i,i**3) for i in range(1,int(input("Enter N: "))+1) ])

