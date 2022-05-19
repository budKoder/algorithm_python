import sys
limit = 10000
arr = [True for _ in range(limit+1)]
arr[0],arr[1] = False, False
for i in range(2,int(limit**0.5)+1):
    if arr[i]:
        for j in range(i+i, limit+1, i):
            arr[j] = False

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a,b = n//2, n//2
    while True:
        if arr[a] and arr[b]:
            print(a,b)
            break
        else:
            a -= 1
            b += 1