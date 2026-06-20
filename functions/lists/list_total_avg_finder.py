def total(sequence):
    result_total = 0
    for i in sequence:
        result_total += i
    return result_total

def length(sequence):
    count = 0
    for _ in sequence:
        count += 1
    return count

def avg(sequence):
    result_total = total(sequence)
    result_length = length(sequence)
    return result_total/result_length

L = [1,2,3,4,5,6,7,8,9,10]
print(total(L))
print(length(L))
print(avg(L))