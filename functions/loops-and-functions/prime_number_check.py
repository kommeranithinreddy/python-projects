def is_prime(number):
    if number <= 1:
        return f'{number} is non prime'
    else:
        count = 0
        for i in range(1, number+1):
            if number % i == 0:
                count += 1
        if count == 2:
            return f'{number} is prime'
        else:
            return f'{number} is non prime'

print(is_prime(4))