def even_gen(start, end):
    for num in range(start, end+1): #easy method is to check if start is even and write 'range(start, end+1, 2)'
        if num%2 == 0:
            yield num


even = even_gen(1, 20)

for value in even:
    print(value)