import sys


def get_th(n):
    for i in range(1,2*n):
        if i*(i+1)/2 >= n and i*(i-1)/2 < n:
            return i

def solution(n):
    th = get_th(n)
    bun = n-int(th*(th-1)/2)
    # 짝수
    if th % 2 == 0:
        up, down = 1,th
        for _ in range(bun-1):
            up+=1
            down-=1
    else:
        up,down = th,1
        for _ in range(bun-1):
            up-=1
            down+=1
    print("{}/{}".format(up,down))


n = int(sys.stdin.readline())
solution(n)