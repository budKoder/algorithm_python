import sys
t = int(sys.stdin.readline())
result = []
for _ in range(t):
    l = list(map(int,sys.stdin.readline().split()))
    l.sort()
    s = set(l)
    if len(s) == 1:
        result.append(10000+l[0]*1000)
    elif len(s) == 2:
        n = l[0] if l[0] == l[1] else l[2]
        result.append(1000+n*100)
    else:
        result.append(l[2]*100)
result.sort()
print(result[-1])