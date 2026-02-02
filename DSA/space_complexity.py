# ✅ Method 1: Using sys.getsizeof()
import sys

arr = [i for i in range(100000)]
print("Memory used by list:", sys.getsizeof(arr))

# ✅ Method 2: Using tracemalloc
import tracemalloc

tracemalloc.start()

arr = [i for i in range(100000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current / 1024:.2f} KB")
print(f"Peak memory: {peak / 1024:.2f} KB")

tracemalloc.stop()

