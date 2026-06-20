def product(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]

    return lst[0] * product(lst[1:])


print(product([]))
print(product([1,2,3,4]))
print(product([3,4,5]))
print(product([1]))