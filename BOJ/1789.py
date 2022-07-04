import sys

s = int(sys.stdin.readline())
s *= 2
for n in range(s):
    if n*(n+1) <= s and (n+1)*(n+2) > s:
        print(n)
        break