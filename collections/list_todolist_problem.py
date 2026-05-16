n = int(input())

for _ in range(1, n+1):
    
    m = int(input())
    inpu = input()
    b = inpu.split()
    c = list(map(int, b))
    d = 0
  
    for i in c:
        if i >= 1000:
            d += 1
    print(d)
