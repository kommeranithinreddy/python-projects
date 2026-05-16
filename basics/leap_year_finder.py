#Write a program to display Leap Year.

year = int(input("Enter year number: "))
print(f'{year} is divisible by 400') if year%400 == 0 else print(f'{year} Leap year as it divisible by 4 and not 100') if year%4 == 0 and year%100 != 0 else print(f'{year} is leap year')
