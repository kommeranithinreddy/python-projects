def list_sum(lst):
    if len(lst) == 0:
        return 0
    #if len(lst) == 1: not needed
        return lst[0]
    else:
        return lst[0] + list_sum(lst[1:])

print(list_sum([1,2,3,4,5]))
print(list_sum([]))
print(list_sum([3]))