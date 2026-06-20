import sys

lst = [i for i in range(1000000)]
gen = (i for i in range(1000000))

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))
