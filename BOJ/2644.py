import sys

n = int(sys.stdin.readline())
graph = [[0 for i in range(n+1)] for j in range(n+1)]
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1

