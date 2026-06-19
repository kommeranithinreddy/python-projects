from time import time
from math import ceil, floor
def outer(function):
    def time_calc():
        start = time()

        function()
        end = time()
        print(end - start) #The value is small. it is in between 0 and 1.
    return time_calc

@outer
def print_function():
    print("Nithin")

print_function()
