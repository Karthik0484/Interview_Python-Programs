''' Usage of Zip
lst1=[2,3,5,7]
lst2=[10,20,30,40]

# print(list(zip(lst1,lst2)))

for i,j in zip(lst1,lst2):
    print(i,j)'''

'''1.Program to Concatenate two lists using zip()'''

lst1=['A','app','','da','kee','t','doc','a']
lst2=['n','le','a','y','ps','he','tor','way']

'''Traditional Approach 
res=[]

for i,j in zip(lst1,lst2):
    res.append(i+j)
print(" ".join(res))  '''

# Using List Comprehension

print(" ".join([i+j for i,j in zip(lst1,lst2) ]))


'''2.Take string sentence as a input and if word length greater than 5 convert to lower else upper'''

'''Traditional Method

s=input("Enter String: ")
lst=s.split()
res=[]

for i in lst:
    if len(i)>5:
        res.append(i.lower())
    else:
        res.append(i.upper())

print(" ".join(res)) '''

# Using List Comprehension

print(" ".join([i.lower() if len(i)>5 else i.upper() for i in input("Enter a String: ").split()]))

