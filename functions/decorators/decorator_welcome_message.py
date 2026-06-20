def parameter(message):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(f'[{message}]')
            function(*args, **kwargs)
        return wrapper
    return decorator

@parameter('INFO')
def login():
    print('User logged in')


login()