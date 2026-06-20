def outer(name):
    def inner():
        return f'Welcome {name}'
    result = inner()
    return result

print(outer("Nithin"))
