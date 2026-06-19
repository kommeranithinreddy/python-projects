def outer(function):
    def inner():
        for _ in range(3):
            function()
    return inner

@outer
def greet():
    print('Hello')

greet()