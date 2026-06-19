def decorator1(function):
    def wrapper1():
        print("Start")
        function()
    return wrapper1

def decorator2(function):
    def wrapper2():
        function()
        print('Welcome')
    return wrapper2

@decorator1
@decorator2
def greet():
    print('Hello Nithin')

greet()