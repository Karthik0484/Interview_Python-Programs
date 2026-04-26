'''Different ways to create the tuple'''

# 1.Using paranthesis
tup =(10,20.5,True,'Python')
print(tup)

# 2.Using in-built function
tupl = tuple()
print(tupl)

# Tuples are immutable in Nature Eg
# tup.append(10) # AttributeError: 'tuple' object has no attribute 'append'

# Slicing the tuple
print(tup[1:3])

# Creating the single element of tuple
a=(10)
print(a) # 10
print(type(a)) # <class 'int'>

b=(10,)
print(b) # (10,)
print(type(b))  # <class 'tuple'>

# Tuple packing
c=10,20,30
print(c) # (10, 20, 30)
print(type(c)) # <class 'tuple'>

# Tuple unpacking
x,y,z=c
print(y) # 20



