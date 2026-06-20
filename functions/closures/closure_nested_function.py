def closure1(a, b):
    def closure2():
        def wrapper():
            print(a,b)
        return wrapper
    return closure2



x = closure1(1, 2)
y = x()
y()