import sys


def solution(n):
    line = 0
    end = 0
    while n > end:
        line += 1
        end += line

    diff = end - n
    print(diff)
    if line%2 == 0:
        top = line - diff
        bottom = 1 + diff
    else:
        top = 1 + diff
        bottom = line - diff
    print("{}/{}".format(top,bottom))


n = int(sys.stdin.readline())
solution(n)