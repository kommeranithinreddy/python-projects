def sorting(sequence, order = False):

    for i in range(1, len(sequence)+1):
        for j in range(len(sequence)-i):
            if order:
                if sequence[j] < sequence[j+1]:
                    sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
            else:
                if sequence[j] > sequence[j+1]:
                    sequence[j], sequence[j+1] = sequence[j+1], sequence[j]

    return sequence


L = [1,4,3,6,7,8,2,9]
print(sorting(L, False))
print(sorting(L, True))
print(sorting(L))