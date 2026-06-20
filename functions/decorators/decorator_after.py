def before(function):
    def wrapper():
        function()
        print('$' * 40)
    return wrapper

@before
def print_name():
    print('Nithin')

print_name()