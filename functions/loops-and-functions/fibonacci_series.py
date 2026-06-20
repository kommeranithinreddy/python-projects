def fibonacci(number):
    result = []
    for i in range(0, number):
        if len(result)<2:
            result.append(i)
        else:
            value = result[-1] + result[-2] #indexing from last
            result.append(value)
    return result

print(fibonacci(10))
