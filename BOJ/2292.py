import sys
n = int(sys.stdin.readline())
tot = 1
cnt = 1
while n > tot:
    tot += 6*cnt
    cnt += 1
print(cnt)