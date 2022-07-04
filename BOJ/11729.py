import sys


def solution(n):
    if n == 1:
        return 1
    else:
        return solution(n-1)*2 + 1


k = int(sys.stdin.readline())
print(solution(k))

