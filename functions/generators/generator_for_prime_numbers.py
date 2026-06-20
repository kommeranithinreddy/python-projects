def prime_generator(stop):
    for num in range(1, stop+1):
        count = 0
        for value in range(1, num+1):
            if num%value == 0:
                count += 1
        if count == 2:
            yield num

prime_nums = prime_generator(29)

print(list(prime_nums))