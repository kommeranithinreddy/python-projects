def largest(sequence):
    largest_element = sequence[0]
    for i in sequence:
        if largest_element<i:
            largest_element = i
    return largest_element

def smallest(sequence):
    smallest_element = sequence[0]
    for i in sequence:
        if smallest_element>i:
            smallest_element = i
    return smallest_element



L = [1,2,4,5,9,10,23,99,98,72]
print(largest(L))
print(smallest(L))