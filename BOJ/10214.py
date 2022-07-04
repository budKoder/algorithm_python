import sys

t = int(sys.stdin.readline())
for _ in range(t):
    y, k = 0,0
    for i in range(9):
        s1, s2 = map(int,sys.stdin.readline().split())
        y += s1
        k += s2
    if y == k:
        print("Draw")
    elif y > k:
        print("Yonsei")
    else:
        print("Korea")