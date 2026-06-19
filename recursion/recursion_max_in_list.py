def max_in_list(lst): # my approach
    if len(lst) == 0:
        return None

    if len(lst) == 1:
        return lst[0]

    if lst[0] <= lst[-1]:
        return max_in_list(lst[1:])

    else:
        return max_in_list(lst[:-1])

print(max_in_list([]))
print(max_in_list([1]))
print(max_in_list([1,2,4,9,5,7,8]))

'''*******************************'''
print('*******************************')

def max_list(lst): #standard recursion
    if len(lst) == 0:
        return None

    if len(lst) == 1:
        return lst[0]

    else:
        return max(lst[0], max_list(lst[1:]))
print(max_in_list([]))
print(max_in_list([1]))
print(max_list([1,2,4,9,5,7,8]))