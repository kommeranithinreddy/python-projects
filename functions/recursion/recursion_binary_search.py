def binary(lst, number):
    if len(lst) == 0:
        return False
    l = len(lst)//2
    if lst[l] == number:
        return True
    elif lst[l] > number:
        return binary(lst[:l], number)
    else:
        return binary(lst[l+1:], number)


print(binary([1, 3, 5, 7, 9, 11, 13, 17], 3))