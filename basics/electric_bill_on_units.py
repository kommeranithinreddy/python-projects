#Electricbill calc
#First 100 units 0 bill
#100 to 200 units 5 per unit
#200 above 10 units

units = int(input("Enter the number of units: "))

a = (units*5) - 500
b = (units*10) - 1500

if units<=100:
    print("Electricity bill is 0")
elif units<=200:
    print(f'Electricity bill is {a}')
else:
    print(f'Electricity bill is {units*10-1500}')
            
