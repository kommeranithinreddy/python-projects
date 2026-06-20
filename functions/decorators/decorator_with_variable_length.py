def decorator(function):
    def inner(*args, **kwargs):
        print(f'Function call started, function name : {function.__name__}')
        return function(*args, **kwargs) #we should return the function if function is returning any value.
    return inner

@decorator
def add(a,b):
    return a+b

@decorator
def student(name, age):
    return f'Student name : {name}, Student age {age}'

print(add(10, 20))
print()
print(student('Nithin', 22))