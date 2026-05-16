n = int(input("Enter: "))

max_value=n
for i in range(0, n+1):
    num = int(input("Enter: "))
    if max_value != None:
        max_value = num
    elif max_value<num:
        max_value = num

print(max_value)

    
