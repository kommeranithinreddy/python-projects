def summation(number):
    result = 0
    while number != 0:
        digit = number%10
        result += digit
        number //= 10
    return result


print(summation(1321))