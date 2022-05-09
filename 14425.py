import sys
n,m = map(int,sys.stdin.readline().split())
s = set()
li = []
for _ in range(n):
    s.add(sys.stdin.readline().strip())
for _ in range(m):
    li.append(sys.stdin.readline().strip())
cnt = 0
for i in range(m):
    if li[i] in s:
        cnt += 1
print(cnt)