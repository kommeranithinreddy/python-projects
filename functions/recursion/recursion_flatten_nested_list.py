def flatten(lst):
    if len(lst) == 0:
        return []

    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])

    else:
        return [lst[0]] + flatten(lst[1:])


x = flatten([1, [2, 3], [4, [5, 6]], 7])
print(x)