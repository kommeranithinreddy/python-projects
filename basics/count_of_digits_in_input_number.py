n = int(input("Enter any number: "))

dig = n
d=0
while dig>0:
    if dig%10:
        d = d+1
    dig = dig//10

print(d)
