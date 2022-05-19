import sys
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    tot = dict()
    for i in range(m):
        c,t = map(str,sys.stdin.readline().split())
        if t in tot:
            tot[t].append(c)
        else:
            tot[t] = [c]
    cnt = 1
    for key in tot.keys():
        cnt *= len(tot[key])+1
    print(cnt-1)