def armstrong_checker(number):
    count = digit_counter(number)
    result = 0
    main_number = number
    while number != 0:
        digit = number % 10
        result = result + digit**count
        number //= 10
    if main_number == result:
        print(f'{main_number} is an armstrong number') #input number should print
    else:
        print(f'{main_number} is not an armstrong number')
    return result

def digit_counter(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count

armstrong_checker(153)