#Amstrong number till n

n = int(input("Enter any number: "))

if n == 0:
    print(n, 'is 0')

for i in range(1, n+1):

    #Calculate power
    dig = i
    d = 0
    while dig>0:
        d = d+1
        dig = dig//10

    #calculate Amstorng
    total = 0
    num = i
    while num>0:
        total = total + (num%10)**d
        num = num//10

    if total == i:
        print("Amstrong is", i)


    
