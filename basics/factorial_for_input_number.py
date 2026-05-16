#Factorial

num = int(input("Enter any number: "))

fact = 1
i = 1

while i<=num:
    fact = fact*i
    i = i + 1

print(f' The factorial of {num} in first method is {fact}')


#Another type
dig = num
into = 1

while dig>0:
    into = into*dig
    dig = dig - 1
print(f' The factorial of {num} in second method is {into}')


#Another type

a = 1
b = 1

while num-a>=0:
    b = b*a
    a = a+1

print(f' The factorial of {num} in third method is {b}')
