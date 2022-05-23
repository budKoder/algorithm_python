import sys
from collections import deque


def solution(graph, q):
    global n,m

    max_day = 0
    while q:
        x,y,day = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx,ny,day+1))
                if day+1 > max_day:
                    max_day = day+1
    return max_day


dx = [1,-1,0,0]
dy = [0,0,1,-1]

m,n = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j,0))
result = solution(graph,q)
isAll = sum(graph[i].count(0) for i in range(n))
if isAll == 0:
    print(result)
else:
    print(-1)