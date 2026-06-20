def validation(function):
    def inner(num1, num2):
        if num1>0 and num2>0:
            return function(num1, num2)
        else:
            return f'Only positive numbers allowed'
    return inner

@validation
def division(n1, n2):
    return n1/n2

print(division(10, 20))
print(division(-10, 20))