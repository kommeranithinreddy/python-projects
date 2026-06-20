def prime_in_range(number):
    for i in range(0, number+1):
        if i > 1:
            count = 0
            for j in range(1, i+1):
                if i%j == 0:
                    count += 1
            if count == 2:
                print(i)

prime_in_range(10)