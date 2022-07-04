import sys
from collections import deque


def bfs(graph, visited):
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m and graph[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    return


dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
bfs(graph,visited)
print(visited[n-1][m-1])
