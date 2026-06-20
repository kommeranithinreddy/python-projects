def summation(number):
    if number <= 0:
        return 0
    else:
        return number + summation(number-1)


print(summation(10))