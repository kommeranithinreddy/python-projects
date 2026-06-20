def parameter(limit):
    count = 0
    def decorator(fun):
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            if count<=limit:
                fun(*args, **kwargs)
            else:
                print('Call limit Exceeded')
        return wrapper
    return decorator


@parameter(3)
def greet(name):
    print(f'Hi, {name}')

greet('nithin')
greet('nandini')
greet('shubham')
greet('santhosh')
greet('sudhamsh')
