def outer():
    seconds = 0
    def inner():
        nonlocal seconds
        seconds += 1
        print(f'{seconds} seconds')
    return inner

seconds = outer()

seconds()
seconds()
seconds()