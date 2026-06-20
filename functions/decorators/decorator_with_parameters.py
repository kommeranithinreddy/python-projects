def parameter(value):
    count = 0
    def decorator(function):
        def wrapper(*args, **kwargs): #why using *args, **kwargs makes it reusable
            nonlocal count
            print('*' * 20)
            for _ in range(value):
                count += 1
                print(count)
                function(*args, **kwargs)
            print('*' * 20)
        return wrapper
    return decorator


@parameter(2)
def greet(name):
    print('Hi', name)

@parameter(2)
def student(id, name):
    print(id, name)


greet('shubham')
print('\n\n')
student('202217b3568', 'Nithin')