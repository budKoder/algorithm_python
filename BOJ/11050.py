import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


n,k = map(int,sys.stdin.readline().split())
result = factorial(n)/(factorial(n-k)*factorial(k))
print(int(result))