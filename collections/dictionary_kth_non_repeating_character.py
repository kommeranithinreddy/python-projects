

S = "geeksforgeeks"
k=2

C = 0
for i in S:
    if S.count(i) == 1:
        C +=1
    if C == k:
        print(i)
        break
