import sys
n = int(sys.stdin.readline().strip())
arr = []

for _ in range(n):
    xy = list(map(int,sys.stdin.readline().split()))
    arr.append(xy)

result = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt+=1
    result.append(cnt)

for r in result:
    print(r, end=" ")