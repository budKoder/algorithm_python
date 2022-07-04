import sys
k = int(sys.stdin.readline())
spot = [[0,0]]
x,y = 0,0
for _ in range(6):
    t,l = map(int,sys.stdin.readline().split())
    if t == 1:
        x += l
    elif t == 2:
        x -= l
    elif t == 3:
        y -= l
    elif t ==4:
        y += l
    spot.append([x,y])
print(spot)