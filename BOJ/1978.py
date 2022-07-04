def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import sys
    n = int(input())
    nums = list(map(int,sys.stdin.readline().split()))
    count = 0
    for num in nums:
        if isPrime(num):
            count+=1
    print(count)