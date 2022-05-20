import sys
sys.setrecursionlimit(10**6)


def dfs(graph, visited, start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph,visited,i)
    return


node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
graph = [[]*node for _ in range(node+1)]
for _ in range(edge):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for _ in range(node+1)]
dfs(graph,visited,1)
print(visited.count(1)-1)