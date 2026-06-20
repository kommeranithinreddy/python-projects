def reversed_number(number):
    result = 0
    while number != 0:
        digit = number%10
        result = result*10 + digit
        number //= 10
    return result

print(reversed_number(9876))