def summation(number):
    total = 0
    for value in range(number+1):
        total += value
    return total

print(summation(5))