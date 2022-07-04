def solution(a,b):
    return sum(range(min(a,b),max(a,b)+1))

a = 3
b = 5
print(solution(a,b))