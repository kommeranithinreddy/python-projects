def generator():
    for i in range(1, 11):
        yield i

numbers = generator()

for num in numbers:
    print(num)
