import sys
from collections import deque

def bfs(graph, a, b):
    global n, m

    q = deque()
    q.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0<= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
    return


dx = [1,-1,0,0]
dy = [0,0,1,-1]

t = int(sys.stdin.readline())
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    graph = [[0 for i in range(m)] for j in range(n)]
    for case in range(k):
        a,b = map(int,sys.stdin.readline().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
                bfs(graph,i,j)
    print(cnt)