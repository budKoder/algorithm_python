import sys
s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
for _ in range(q):
    prefix_sum = [0]
    a,l,r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    for i in range(len(s)):
        if s[i] == a:
            prefix_sum.append(prefix_sum[i]+1)
        else:
            prefix_sum.append(prefix_sum[i])
    print(prefix_sum[r+1]-prefix_sum[l])