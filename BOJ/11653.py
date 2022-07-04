import sys
n = int(sys.stdin.readline())

m = 2
while n > 1:
    if n%m == 0:
        print(m)
        n //= m
    # 루트 n 이하에서 더이상 나누어 떨어지는 수가 없다면 남은 수는 소수
    elif m > n**0.5:
        print(int(n))
        break
    else:
        m+=1