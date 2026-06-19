#Candies disribution

T = int(input("Enter your number: "))

if 1<=T<=100:
    for _ in range(T):
        N = int(input("Number of candies: "))
        if 1<=N<=100 :
            if N%3 == 0:
                print("Yes")
            else:
                print("No")



