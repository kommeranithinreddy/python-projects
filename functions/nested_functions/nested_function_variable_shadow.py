def outer():
    outer = 4
    def inner():
        inner = 5
        outer = 10
        print(outer)
        print(inner)
    inner()
    return outer

print(outer())