def square_generator():
    num=1
    while True:
        yield num ** 2
        num += 1

square = square_generator()

for _ in range(10):
    print(next(square))

print()
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
