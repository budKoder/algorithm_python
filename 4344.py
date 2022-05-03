import sys


def get_avg(scores):
    sum = 0
    for s in scores:
        sum += s
    return sum/len(scores)


c = int(sys.stdin.readline())
for _ in range(c):
    arr = list(map(int,sys.stdin.readline().split()))
    n = arr[0]
    scores = arr[1:]
    avg = get_avg(scores)
    cnt = 0
    for s in scores:
        if s > avg:
           cnt += 1
    print("{:.3f}%".format(cnt/n*100))