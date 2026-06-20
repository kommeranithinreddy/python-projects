def reverse_num(num, result_num = 0): #329
    if num == 0:
        return result_num
    result_num = num % 10 + result_num * 10
    return reverse_num(num//10, result_num)



result = reverse_num(int(input('Enter your number: ')))
print(result)