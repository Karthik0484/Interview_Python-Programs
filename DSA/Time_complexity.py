# ✅ Method 1: Using time module
'''import time

def linear_search(arr,target):
    for i in arr:
        if i == target:
            return True
    return False

arr = list(range(10_00_0000))

start=time.time()
linear_search(arr, 99999999)
end = time.time()

print("Total time taken: ",end-start)'''

# ✅ Method 2: Compare Two Algorithms (Best for Understanding)

import time

def sum_loop(n):
    s = 0
    for i in range(n):
        s += i
    return s

def sum_formula(n):
    return n * (n - 1) // 2

n = 10_000_000

start = time.time()
sum_loop(n)
print("Loop time:", time.time() - start)

start = time.time()
sum_formula(n)
print("Formula time:", time.time() - start)


