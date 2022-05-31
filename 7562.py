import sys
from collections import deque

available = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
t = int(sys.stdin.readline())
for _ in range(t):
    l = int(sys.stdin.readline())
    fr_x, fr_y = map(int,sys.stdin.readline().split())
    to_x, to_y = map(int,sys.stdin.readline().split())

    graph = [[0 for i in range(l)] for j in range(l)]
    graph[fr_x][fr_y] = 1
    dq = deque()
    dq.append([fr_x, fr_y])
    while dq:
        cur_x, cur_y = dq.popleft()
        if cur_x == to_x and cur_y == to_y:
            print(graph[to_x][to_y] -1)
            break

        for x,y in available:
            nx = cur_x + x
            ny = cur_y + y
            if 0<=nx<l and 0<= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[cur_x][cur_y] + 1
                dq.append([nx,ny])