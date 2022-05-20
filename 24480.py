import sys
sys.setrecursionlimit(10**6)


def dfs(graph, visited, start):
    global cnt
    visited[start] = cnt
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph,visited,i)
    return


n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort(reverse=True)

visited = [0 for _ in range(n+1)]
cnt = 1
dfs(graph,visited,r)
for i in range(1,n+1):
    print(visited[i])