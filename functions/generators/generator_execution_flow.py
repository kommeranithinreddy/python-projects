def generator():
    print('before yeild')
    yield 'during yeild'
    print('after yield')
    yield 10

gen = generator()
print(next(gen))
print(next(gen))

