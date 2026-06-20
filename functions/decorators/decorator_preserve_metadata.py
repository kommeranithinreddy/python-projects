from functools import wraps


def decorator(function):
    @wraps(function)  #wraps is a decorator in functools
    def wrapper():
        '''This is the wrapper function'''
        print('*******')
        function()
    print(wrapper.__name__)
    return wrapper


@decorator
def greet():
    '''This function greet the user'''
    print('Hi')


print(greet.__name__)
print(greet.__doc__)
greet()