import sys
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = [i+1 for i in range(n)]

    for i in range(1,k+1):
        sum = 0
        for j in range(n):
            sum += arr[j]
            arr[j] = sum
    print(arr[n-1])