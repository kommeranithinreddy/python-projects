def second_largest_number(sequence):
    largest =sequence[0]
    for i in sequence:
        if i > largest:
            largest = i
    second_largest = None
    for i in sequence:
        if second_largest == None:
            if i<largest:
                second_largest = i
        else:
            if second_largest<i<largest:
                second_largest = i
    return second_largest

L = [900,2,3,4,5,6,7, 9, 7]
print(second_largest_number(L))