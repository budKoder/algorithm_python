import sys


def solution(x,y):
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x>0 and y<0:
        return 4
    else:
        return 0


n = int(sys.stdin.readline())
result = [0,0,0,0,0]
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    q = solution(x,y)
    result[q] += 1
for i in range(1,5):
    print("Q{}: {}".format(i,result[i]))
print("AXIS: {}".format(result[0]))