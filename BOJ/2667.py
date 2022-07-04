import sys
from collections import deque


def bfs(graph, visited, n, x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx,ny))
    return cnt


n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[0 for i in range(n)] for j in range(n)]
result = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == 0:
           result.append(bfs(graph,visited,n,x,y))
print(len(result))
result.sort()
for r in result:
    print(r)
