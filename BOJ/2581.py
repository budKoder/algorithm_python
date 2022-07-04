import sys


def isPrime(n):
    arr = [True for _ in range(n+1)]
    arr[0],arr[1] = False, False
    for i in range(2,int(n**0.5)+1):
        for j in range(i*2, n+1, i):
            arr[j] = False
    return arr


def solution(arr, m, n):
    result = []
    for i in range(m,n+1):
        if arr[i]:
            result.append(i)
    return result


m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
arr = isPrime(n)
result = solution(arr,m,n)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))