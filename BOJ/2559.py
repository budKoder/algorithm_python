import sys
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
prefix_sum = []
sum = 0
for i in range(k):
    sum += arr[i]
prefix_sum.append(sum)
for i in range(1,n-k+1):
    num = prefix_sum[i-1]-arr[i-1]+arr[i+k-1]
    prefix_sum.append(num)
print(max(prefix_sum))