import sys
n,w,h = map(int,sys.stdin.readline().split())
mx = int((w**2 + h**2)**0.5)
for _ in range(n):
    length = int(sys.stdin.readline())
    if length > mx:
        print("NE")
    else:
        print("DA")