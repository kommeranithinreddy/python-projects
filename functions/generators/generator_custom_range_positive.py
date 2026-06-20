def custom_range(start, stop, step):
    num = start
    while num < stop:
        yield num
        num += step

gen = custom_range(2, 20, 2)

for i in gen:
    print(i)