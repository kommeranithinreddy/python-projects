#Piligriam Test

num = int(input("Enter your number: "))

test = num
power = 0
pil = 0
dig = num

while test>0:
    power += 1
    test//=10

while num>0:
    value = num%10
    pil = pil + value * 10**(power-1)
    power -= 1
    num = num//10

if pil == dig:
    print (f"{dig} is a piligram")
else:
    print(f"{dig} is *not* a piligram")
