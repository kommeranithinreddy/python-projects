def generator():
    yield 1
    yield 2
    yield 3

test_gen = generator()

try:
    print(next(test_gen))
    print(next(test_gen))
    print(next(test_gen))
    print(next(test_gen)) # 4th call -> raises StopIteration
    print(next(test_gen)) # 5th call >> never executes

except StopIteration:
    print("Generator Completed")