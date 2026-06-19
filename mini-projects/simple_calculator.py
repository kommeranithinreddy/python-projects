def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

def calculator(a,b, calc_type = 'add'):
    match calc_type:
        case 'add':
            return add(a,b)
        case 'sub':
            return sub(a, b)
        case 'mul':
            return multi(a, b)
        case 'div':
            return div(a, b)
        case _:
            return "invalid type"

print(calculator(1,2, 'div'))