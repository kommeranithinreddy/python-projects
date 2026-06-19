def before(function):
    def wrapper():
        print('$' * 40)
        function()
    return wrapper

@before
def print_name():
    print('Nithin')

print_name()