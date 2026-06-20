def summation(num):
    if num // 10 == 0:
        return num
    else:
        return num%10 + summation(num//10)


print(summation(10))
print(summation(1234))

