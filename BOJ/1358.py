import sys


def isInCircle(x,y,a,b,r):
    d = ((x-a)**2 + (y-b)**2)**0.5
    if d <= r:
        return True
    return False


w,h,x,y,p = map(int,sys.stdin.readline().split())
r = h/2
cnt = 0
for _ in range(p):
    a,b = map(int,sys.stdin.readline().split())
    if x <= a <= x+w and y <= b <= y+h:
        cnt += 1
    elif isInCircle(x,y+r,a,b,r) or isInCircle(x+w,y+r,a,b,r):
        cnt += 1
print(cnt)