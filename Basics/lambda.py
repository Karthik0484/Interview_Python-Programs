res=(lambda num,p:num**p)(5,3)
print(res)

# Using lambda function multiple times
fun1=lambda num,den:num/den

res=fun1(10,2)
print(res)

res2=fun1(20,10)
print(res2)

# Map function
lst=[1,2,3,4,5]

def fun(x):
    return x**2

res=list(map(fun,lst))
print(res)

# Map using lambda function

sq_list= list(map(lambda x:x**2,lst))
print(sq_list)

def fun1(num):
    return lambda  x:x*num

print(fun1(2)(5))

# Using function multiple times
fun2=fun1(2)
res=fun2(10)
print(res)

# Program for mathematical table of any given number

n=int(input("Enter a number:\n"))

math_table=fun1(n)
for i in range(1,11):
    print(n,'X',i,'=',math_table(i))