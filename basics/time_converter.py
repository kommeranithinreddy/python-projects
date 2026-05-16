#Time Converter (Seconds to H:M:S)
#Convert seconds to hours, minutes, and seconds format.

value = int(input("Enter your seconds: "))

Hours = value//3600
value2 = value%3600
Minutes = value2//60
Seconds=value2%60

print(f'H - {Hours} : M - {Minutes} : S - {Seconds}')
print(f'{Hours} : {Minutes} : {Seconds}')
