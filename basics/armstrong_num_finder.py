#Find the Amstrong number


num = int(input("Enter your number: "))

count = num
org = num
leng = 0
Sum = 0

while count>0:
    leng = leng + 1
    count = count//10

while num>0:
    rem = num%10
    Sum = Sum + (rem**leng)
    num = num//10

if org == Sum:
    print(f'{org} is amstrong number')
else:
    print(f'{org} is not amstrong number')
