import sys
limit = 123456
arr = [True for _ in range(2*limit+1)]
arr[0],arr[1] = False, False
for i in range(2,int((2*limit)**0.5+1)):
    if arr[i]:
        for j in range(i+i, 2*limit+1, i):
            arr[j] = False
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(arr[n+1:2*n+1].count(True))