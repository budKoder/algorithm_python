import sys
n = int(sys.stdin.readline())
factorial = 1
for i in range(n,0,-1):
        factorial *= i
cnt = 0
while factorial>1:
    if factorial % 10 == 0:
        cnt += 1
        factorial //= 10
    else:
        break
print(cnt)