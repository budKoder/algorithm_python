import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()
start = 1
end = max(x) - min(x)
while start <= end:
    mid = (start+end)//2
    loc = x[0]
    cnt = 1
    for i in range(1,len(x)):
        if x[i] - loc >= mid:
            loc = x[i]
            cnt += 1

        if cnt >= c:
            break

    if cnt >= c:
        start = mid+1
    else:
        end = mid-1
print(end)