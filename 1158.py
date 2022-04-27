import sys
n, k = map(int,sys.stdin.readline().split())
arr = [_+1 for _ in range(n)]
result = []
idx = -1
while len(arr)>0:
    idx += k
    idx %= len(arr)
    result.append(str(arr[idx]))
    del arr[idx]
    idx -= 1
print("<"+", ".join(result)+">")
