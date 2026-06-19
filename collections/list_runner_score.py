
n = int(input("Enter number of players: "))

L = []
for _ in range(n):
    score = int(input("Enter scores: "))
    L.append(score)

L.sort()
n = len(L)

for i in range(n-1, 0, -1):
    if L[i]>L[i-1]:
        print(f'The runner up score is {L[i-1]}')
        break
    
    if i<=1:
        print("All score are equal & scores are", L)

if n == 1:
    print('Only one score is provided, scores = ', score)
