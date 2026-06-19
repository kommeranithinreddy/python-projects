def custom_range(start, stop, step=1):
    if step > 0:
            num = start
            while num < stop:
                yield num
                num += step
    elif step < 0:
            num = start
            while num > stop:
                yield num
                num += step

positive  = custom_range(1, 20)
negative = custom_range(20, 1, -1)

print(list(positive))
print(list(negative))