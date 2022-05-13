import sys
t = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
li.sort()
if t == 1:
    print(li[0]*li[0])
else:
    print(li[0] * li[-1])