import sys
n = int(sys.stdin.readline())

sum = 0
scores = list(map(int,sys.stdin.readline().split()))
m = max(scores)

for s in scores:
    sum += (s/m) * 100
print(sum/n)