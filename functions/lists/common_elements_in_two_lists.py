def common_elements_in_two_lists(sequence1, sequence2):
    common_elements = []
    for i in sequence1:
        if i in sequence2 and i not in common_elements:
            common_elements.append(i)

    return common_elements


L1 = [1,2,3,4,5,6,7,8,9,9]
L2 = [7,8,9,10,11]
print(common_elements_in_two_lists(L1, L2))
