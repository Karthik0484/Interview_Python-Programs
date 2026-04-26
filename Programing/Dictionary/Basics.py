'''d={1:'a',2:[10,20,30]}
print(d)

x=d[1]
print(x)  # a
x='b'
print(x) # b
y=d[2]
print(y) # [10, 20, 30]
y.append(40)
print(y) #  [10, 20, 30, 40]
print(d) #  {1: 'a', 2: [10, 20, 30, 40]}
'''

'''1.WAP to count occurrence of each character in the given string

str='Python Programming'
d={}
for i in str.lower():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d) '''

'''2.WAP to print mobile number associated with name , if name is not in entry then display contact not found
3
charlie 876543210
Bob 9876543210
Rock 8907654321
2
bob
mob:  9876543210
rock
mob:  8907654321

n=int(input())
d={}

for i in range(n):
    lst=input().split()
    d[lst[0].lower()] = lst[1]

s=int(input())

for i in range(n):
    name=input().lower()
    if name in d:
        print("mob: ",d[name])
    else:
        print("Contact not found.") '''

'''4.WAP to print kth non-repeating character in given string.
karthik
2
r 

s=input()
n=int(input())
d={}
count=0

for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

for ch in d:
    if d[ch]==1:
        count+=1
        if n==count:
            print(ch)
            break '''

'''5.WAP to print occurrence of each word in a given sentence
import re

s=input().lower()
s=re.sub(r'[!?.]','',s)
lst=s.split()
d={}

for i in lst:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

for i in d:
    if d[i]>=3:
        print(i) '''

'''6.WAP to print highest marks of every person
karthik 80,alice 90, karthik 85,bob 90
{'KARTHIK': '85', 'ALICE': '90', 'BOB': '90'} 

s=input().split(",")
d={}

for i in s:
    lst=i.split()
    name=lst[0].upper()
    marks=int(lst[1])

    if name not in d:
        d[name]=marks
    else:
        if marks>d[name]:
            d[name]=marks
print(d) '''

'''7.WAP to inverse the dictionary ub such a way that keys become values and values become keys
I/P: {1: 'A', 2: 'B', 3: 'C', 4: 'A', 5: 'B', 6: 'B'}
O/P: {'A': [1, 4], 'B': [2, 5, 6], 'C': [3]} 

d={1:'A',2:'B',3:'C',4:'A',5:'B',6:'B'}
res={}

for i in d:
    if d[i] not in res:
        res[d[i]] = []
        res[d[i]].append(i)
    else:
        res[d[i]].append(i)

print(d)
print(res) '''

'''8.WAP that splits the sentence and arrange them in descending order based on length then arrange them in chronological order.'''

s=input().lower().split()
res={}

for i in s:
    if len(i) not in res:
        res[len(i)]=[]
        res[len(i)].append(i)
    else:
        res[len(i)].append(i)

for i in sorted(res.keys(), reverse=True):
    for j in sorted(res[i]):
        print(j)

print(res)






