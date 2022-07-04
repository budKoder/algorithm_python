import sys
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(10)]
x,y = 1,1
graph[x][y] = 9
while True:
    item = 0
    if graph[x][y+1] != 1:
        y += 1
        item = graph[x][y]
        graph[x][y] = 9
    elif graph[x+1][y] != 1:
        x += 1
        item = graph[x][y]
        graph[x][y] = 9
    elif graph[x][y+1] == 1 and graph[x+1][y] == 1:
        break

    if item == 2:
        break
for g in graph:
    print(*g)