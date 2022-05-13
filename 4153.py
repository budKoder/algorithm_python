import sys
while True:
    li = list(map(int,sys.stdin.readline().split()))
    if li[0] == 0 and li[1] == 0 and li[2] == 0:
        break
    mx = max(li)
    li.remove(mx)
    a = li[0]
    b = li[1]
    if mx**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")