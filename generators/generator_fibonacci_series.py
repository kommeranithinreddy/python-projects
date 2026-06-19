def fibonacci(number):
    num1 = 0
    num2 = 1
    for _ in range(number):
        yield num1
        temp = num2
        num2 = num1 + num2
        num1 = temp

f10 = fibonacci(10)

for i in f10:
    print(i, end = '\t')



