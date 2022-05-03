import sys
import math

a,b,c = map(int,sys.stdin.readline().split())

if c-b <= 0:
    print(-1)
else:
    cnt = math.floor(a/(c-b))+1
    print(cnt)