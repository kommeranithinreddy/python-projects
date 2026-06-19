#Amstrong number from 100 to 99



for i in range(99, 1000):
    value = i
    num = 0
    while i > 0:
        d = i%10
        i = i//10
        num = num + d**3

    if num == value:
        print ("Amstrong", value)

#********



        
