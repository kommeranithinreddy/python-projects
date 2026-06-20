def is_perfect(number):
    divisors = list_of_divisors(number)
    if sum(divisors) == number:
        print(f'{number} is perfect number')
    else:
        print(f'{number} is not a perfect number')

def list_of_divisors(number):
    result = []
    for i in range(1, number):
        if number%i == 0:
            result.append(i)
    return result

is_perfect(8128)