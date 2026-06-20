def outer(name):
    def inner(greetings):
        user_name = name
        print(f'{greetings} {user_name}')
    return inner


greet = outer('Nithin')
greet('Welcome')
greet('How are you')
greet("I hope you're doing well")
