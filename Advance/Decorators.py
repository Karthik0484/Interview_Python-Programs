'''1.Function that return another function Eg
def get_sum(lst):
    print(sum(lst))

def product(lst):
    p=1
    for i in lst:
        p*=i
    return p

def choice(user):
    if user == 'sum':
        return get_sum
    else:
        return product

fun1=choice('sum')
fun1([1,2,3,4,5])
fun2=choice('product')
print(fun2([1,2,3,4,5])) '''

'''2.Decorator function that returns product of of squares of given list of numbers

def decorator(num):
    def power_of(ref):
        def wrapper(lst):
            lst = list(map(lambda x: x ** num, lst))
            ref(lst)
        return wrapper
    return power_of

@decorator(3)
def getProduct(lst):
    p=1
    for i in lst:
        p*=i
    print(p)

# fun1=decorator(3)
# fun2=fun1(getProduct)
# fun2([1,2,3,4,5])

getProduct([1,2,3,4,5]) '''

'''3.Closure concept'''

def outer():
    x=99

    def inner1():
        y=88

        def inner2():
            print(x)
            print(y)
        return inner2()
    return inner1()

fun1=outer
fun2=fun1
fun2()
del outer
del fun1
fun2()






