import sys

n = int(sys.stdin.readline())
s1, s2 = 100,100
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    if x == y:
        continue
    elif x > y:
        s2 -= x
    elif x < y:
        s1 -= y
print(s1)
print(s2)