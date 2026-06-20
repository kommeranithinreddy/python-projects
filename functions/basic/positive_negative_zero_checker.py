def checker(num):
    if num>0:
        print(f'{num} is positive')
    elif num<0:
        print(f'{num} is negative')
    else:
        print(f'{num} is Zero')

checker(int(input("Enter any number: ")))