#Check 2 number and print the larger one using CLR
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(num1+num2)
print(f'{num1} is greater') if num1>num2 else print(f'{num2} is greater') if num2>num1 else print("both the numbers are equal")
