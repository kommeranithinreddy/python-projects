#Speed Converter (km/h to m/s)
#Convert speed from kilometers per hour to meters per second.

#1 KM is 1000 meters
#1 HR is 3600 seconds

skm = float(input("Enter speed in KM/H: "))

sms = round(skm*0.277778, 2)

print(f'Speed in Mtr/sec is {sms} m/s')
