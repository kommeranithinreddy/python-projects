def counter(function):
    count = 0
    def wrapper():
        nonlocal count
        count+=1
        function()
        print(f'function {function.__name__} called {count} times')
    return wrapper

@counter
def greet():
    print('Hello user')

greet()
greet()
greet()
greet()