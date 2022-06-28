def solution(n):
    result = set(map(lambda x:x if n%x==0 else 0, range(1,n+1)))
    return sum(result)