def duplicate_remover(sequence):
    new_list = []
    for i in sequence:
        if i not in new_list:
            new_list.append(i)
    return new_list

L = [1,1,1,1,1,2,3,4,5,6,7,8,8,8,8]
print(duplicate_remover(L))