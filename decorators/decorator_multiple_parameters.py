def parameter(char, length):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(char*length)
            function(*args, **kwargs)
            print(char*length)
        return wrapper
    return decorator

@parameter('#', 50)
def greet(message, name):
    print(f'"{message}" message is received for user : {name}')

greet('Welcome to the project', 'Nithin')