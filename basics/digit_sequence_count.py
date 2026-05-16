#count of specific digit

num = int(input("Enter any number : "))
i = int(input("Enter number to find the sequence: "))
dig = num
count = 0

while dig>0:
   if  i == dig%10:
       count += 1

   dig = dig//10

print(f'{i} is repeated {count} times in {num}')
    
