
'''1.WAP to print length of each word.
India USA Japan
{'India': 5, 'USA': 3, 'Japan': 5}
s=input().split()
res={i:len(i) for i in s}

print(res) '''

'''2.WAP 
# Using traditional method

lst=['India','USA','poland','Japan']
res={}

for i in lst:
    if len(i)<6:
        if len(i)%2==0:
            res[i.upper()] = len(i) ** 2
        else:
            res[i.upper()] = len(i) ** 3
    else:
        if len(i) % 2 == 0:
            res[i.lower()] = len(i) ** 2
        else:
            res[i.lower()] = len(i) ** 3

print(res) 

# Using dictionary comprehension
lst=['India','USA','poland','Japan']
res={(i.upper() if len(i)<6 else i.lower()):(len(i)**2 if len(i)%2==0 else len(i)**3) for i in lst}
print(res) '''




