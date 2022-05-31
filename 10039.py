import sys
sum = 0
for _ in range(5):
    n = int(sys.stdin.readline())
    if n < 40:
        sum += 40
    else:
        sum += n
print(int(sum/5))