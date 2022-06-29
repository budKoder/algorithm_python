def solution(x):
    n = x
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    return True if x%sum == 0 else False

x = 11
print(solution(x))