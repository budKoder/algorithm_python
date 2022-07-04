import sys


def getDivisor(n):
    divisor = []
    for i in range(1,n):
        if n%i == 0:
            divisor.append(i)
    return divisor


while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    divisor = getDivisor(n)
    if sum(divisor) == n:
        print(n,"= ",end="")
        print(" + ".join(map(str,divisor)))
    else:
        print(n,"is NOT perfect.")
