def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    return inner

counter1 = outer()
counter2 = outer()

counter1()
counter2()
counter1()
counter2()
counter2()
counter2()
counter1()

