import sys


def solution(e,s,m):
    if e == s and s == m:
        return e
    else:
        p = 0
        q = 0
        while True:
            q = 28 * p + s
            if q % 15 == e and q % 19 == m:
                break
            p += 1
        return q


e,s,m = map(int,sys.stdin.readline().split())
e = 0 if e % 15 == 0 else e
m = 0 if m % 19 == 0 else m
print(solution(e,s,m))