import sys

t = int(sys.stdin.readline())
for _ in range(t):
    values = dict()
    n = int(sys.stdin.readline())
    for i in range(n):
        s,l = map(str,sys.stdin.readline().split())
        if s in values:
            values[s] += int(l)
        else:
            values[s] = int(l)
    values = sorted(values.items(), key=lambda x:x[1], reverse=True)
    print(values[0][0])