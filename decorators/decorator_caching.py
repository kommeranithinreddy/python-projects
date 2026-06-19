def cache(fun):
    cache_dict = {}
    def wrapper(value): #This decorator supports functions with one positional argument.
        if value in cache_dict:
            print("Using Cached Value......")
            print(cache_dict[value])
        else:
            res = fun(value)
            print(res)
            cache_dict[value] = res
    return wrapper

@cache
def square(num):
    return num*num

square(5)
square(5)
square(10)
square(10)