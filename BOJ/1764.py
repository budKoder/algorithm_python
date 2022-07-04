import sys
n,m = map(int,sys.stdin.readline().split())
ns, ms = set(), set()
for _ in range(n):
    ns.add(sys.stdin.readline().strip())
for _ in range(m):
    ms.add(sys.stdin.readline().strip())
result = list(ns.intersection(ms))
result.sort()
print(len(result))
for name in result:
    print(name)