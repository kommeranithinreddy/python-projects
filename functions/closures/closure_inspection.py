def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    return inner


counter = outer()
print(counter.__closure__)
print(counter.__closure__[0].cell_contents)