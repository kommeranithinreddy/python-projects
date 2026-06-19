L = ["nithin", "reddy", "kommera", "gond", "shubham", "juttu", "nandini"]

max = 0
for value in L:
    if len(value) > max:
        max = len(value)
        i = L.index(value)

print(max, L[i])
        
        
