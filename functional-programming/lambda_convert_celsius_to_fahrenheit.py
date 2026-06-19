cels_to_fahren = lambda cel: (cel*1.8) + 32
fahren_to_cels = lambda fahr: (fahr - 32)/1.8

print(cels_to_fahren(int(input("Enter Celsius to convert: "))))
print(fahren_to_cels(int(input("Enter Fahrenheit to convert: "))))