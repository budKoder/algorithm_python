import sys

t = int(sys.stdin.readline())
tm = [300,60,10]
n = [0,0,0]
for i in range(3):
    n[i] += t//tm[i]
    t %= tm[i]
if t != 0:
    print(-1)
else:
    print(*n)