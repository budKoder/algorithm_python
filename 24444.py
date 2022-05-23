import sys
from collections import deque


def bfs(graph, visited,r):
    q = deque([r])
    cnt = 1
    visited[r] = cnt
    while q:
        u = q.popleft()
        for i in graph[u]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)
    return


n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
bfs(graph,visited,r)

for i in range(1,n+1):
    print(visited[i])