import sys
h,m,s = map(int,sys.stdin.readline().split())
d = int(sys.stdin.readline())

total = h*60*60 + m*60 + s + d
ns = total%60
total //= 60
nm = total%60
total //= 60
nh = total%24

print(nh, nm, ns)