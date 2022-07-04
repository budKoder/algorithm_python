import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    h,w,n = map(int,sys.stdin.readline().split())
    xx = math.ceil(n/h)
    yy = h if n%h==0 else n%h
    print(str(yy) + str(xx).zfill(2))