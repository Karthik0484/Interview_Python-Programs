'''1.WAP to print squares of a number in set
s={5,4,8,9,6}
# Traditional Approach
res=set()
for i in s:
    res.add(i**2)
print(s)
print(res)

# Using set comprehension
res={i**2 for i in s }
print(res) '''

'''2.WAP to squares of only even numbers in the list
# Traditional Approach
s={5,4,8,9,6}
res=set()
for i in s:
    if i%2==0:
        res.add(i**2)
print(res)

# Using set comprehension
print({i**2 for i in s if i%2==0}) '''

'''3.WAP to print square of number if even else increment by one
# Traditional Approach
s={5,4,8,9,6}
res=set()
for i in s:
    if i%2==0:
        res.add(i**2)
    else:
        res.add(i+1)
print(res)

# Using set comprehension
print({i**2 if i%2==0 else i+1 for i in s}) '''

s='The quick brown fox jumps over lazy dog'.upper()

'''4.Check if a string is pangram or not

# Traditional method
res=set()
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        res.add(i)

if  len(res)==26:
    print(s,'is a pangram')
else:
    print(s, 'is not a pangram') 

# Using set comprehension
if len({i for i in s if ord(i)>=65 and ord(i)<=90 })==26:
    print(s,'is a pangram')
else:
    print(s,'is a pangram') '''

str='The big dwarf only jumps'.upper()
'''5. Check if the string is heterogram

# Traditional Approach 
res=[]
for i in str:
    if ord(i)>=65 and ord(i)<=90:
        res.append(i)
c= {i for i in str if ord(i)>=65 and ord(i)<=90}

if len(res)==len(c):
    print(str,'is a Heterogram.')
else:
    print(str,'is not a heterogram.') 

# Using set comprehension

if len([i for i in str if ord(i)>=65 and ord(i)<=90])==len({i for i in str if ord(i)>=65 and ord(i)<=90}):
    print(str, 'is a heterogram')
else:
    print(str,'is not a heterogram') '''





