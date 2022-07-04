import sys
n = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))
d = dict()
for c in cards:
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1

m = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
result = []
for x in li:
    if x in d:
        result.append(d[x])
    else:
        result.append(0)

print(*result)