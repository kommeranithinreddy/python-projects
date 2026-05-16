

d =  [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10}, {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19}, {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}]
K = "Gfg"
idx = 1

for i in range(len(d)):
    for j in range(len(d)):
        if d[i]["Gfg"][idx] < d[j]["Gfg"][idx]:
            d[i], d[j] = d[j],d[i]
print(d)
