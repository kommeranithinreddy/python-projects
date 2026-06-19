#Write a program to find set and unset bits
#In a given number

num = int(input("Enter any number: "))

dig = num
zero = 0
one = 0

if num == 0:
    zero = 1

while num > 0:
    if num%2 == 0:
        zero = zero + 1
    else:
        one = one + 1

    num = num//2

print(f'number of zeros in {dig} are {zero} and ones are {one}')
