import sys
n,m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(height)
while start <= end:
    mid = (start+end)//2
    tot = 0
    for h in height:
        if h > mid:
            tot += h - mid
        if tot >= m:
            break
    if tot >= m:
        start = mid+1
    else:
        end = mid-1
print(end)