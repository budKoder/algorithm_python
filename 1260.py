import sys
from collections import deque


def dfs(graph, visited, v, result):
    global cnt
    cnt += 1
    visited[v] = cnt
    result.append(v)
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph,visited,i,result)
    return


def bfs(graph, visited, v, result):
    cnt = 1
    visited[v] = cnt
    q = deque([v])
    result.append(v)
    while q:
        u = q.popleft()
        for i in graph[u]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)
                result.append(i)
    return

n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visited = [0 for _ in range(n+1)]
cnt = 0
result = []
dfs(graph,visited,v,result)
print(*result)
visited = [0 for _ in range(n+1)]
result = []
bfs(graph,visited,v,result)
print(*result)