def factorial(number):
    result = 1
    for value in range(number, 0, -1):
        result *= value
    return result

print(factorial(3))