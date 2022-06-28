def solution(n):
    arr = list(range(n))
    return ''.join(list(map(lambda x:'수' if x%2 == 0 else '박',arr)))

n = 4
print(solution(n))