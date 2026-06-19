n = int(input())

arr = set(map(int, input().split()[:n]))

x = int(input())

if x in arr:
    arr.remove(x)
    print("erased x")
else:
    print('not found')

print(arr)
