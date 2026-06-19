def max_finder(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            print(f'{num1} is the maximum')
        else:
            print(f'{num3} is the maximum')
    else:
        if num2>num3:
            print(f'{num2} is the maximum')
        else:
            print(f'{num3} is the maximum')

max_finder(3,2,1)