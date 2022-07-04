import sys
n = int(sys.stdin.readline())
for _ in range(n):
    r,e,c = map(int,sys.stdin.readline().split())
    if e-c > r:
        print('advertise')
    elif e-c == r:
        print("does not matter")
    else:
        print("do not advertise")