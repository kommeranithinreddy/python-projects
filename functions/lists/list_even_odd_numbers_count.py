def even_odd_counter(sequence):
    even_count = 0
    odd_count = 0
    for i in sequence:
        if i%2==0:
            even_count += 1
        else:
            odd_count += 1

    print(f'Even count is {even_count}')
    print(f'Odd count is {odd_count}')

L = [1,2,3,4,5,6,7,8,9,10]
even_odd_counter(L)