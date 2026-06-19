#Find maximum and minimum in given number

num = int(input("Enter your number: "))

mini = num #Don't take 9 to avoid zero input
maxi = 0

while num > 0:
    d = num%10
    if maxi < d:
        maxi = d
    if mini > d: #only if not elif
        mini = d

    num = num//10

print(f'{maxi} is maximum and {mini} is minimum')
