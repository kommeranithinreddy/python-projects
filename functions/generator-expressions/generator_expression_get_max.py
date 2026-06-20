from random import randint

generator = (randint(1, 999999) for _ in range(10))

print(max(generator))