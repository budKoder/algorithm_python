import sys
from collections import deque


def solution(graph,q):
    global n,m,h
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz,nx,ny))
    return


dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

m,n,h = map(int,sys.stdin.readline().split())
graph = []
for _ in range(h):
    floor = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
    graph.append(floor)

q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append((k,i,j))
solution(graph,q)
isAll = sum(sum(graph[k][i].count(0) for i in range(n)) for k in range(h))
if isAll == 0:
    mx = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                mx = max(mx, graph[k][i][j])
    print(mx-1)
else:
    print(-1)