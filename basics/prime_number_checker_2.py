#Prime number check

num = int(input("Enter your number: "))


i=2
div = 0
while i<num and div == 0:
    if num%i == 0:
        div = div + 1
    i = i + 1

if num == 0 or num == 1:
    print("non prime")
elif div == 0:
    print ("prime")
else:
    print("non prime")
