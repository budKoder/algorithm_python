import sys
n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
sum = [0]
for i in range(len(arr)):
    if i == 0:
        sum.append(arr[i])
    else:
        sum.append(sum[i]+arr[i])

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(sum[b]-sum[a-1])