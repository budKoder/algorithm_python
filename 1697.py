import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
mx = 100000
graph = [0 for _ in range(mx+1)]
graph[n] = 1
dq = deque([n])
while dq:
    cur = dq.popleft()
    if cur == k:
        print(graph[k]-1)
        break
    for l in [cur-1, cur+1, cur*2]:
        if 0<=l<=mx and graph[l] == 0:
            graph[l] = graph[cur]+1
            dq.append(l)