def solution(n):
    if int(n**0.5) == n**0.5:
        return (1+int(n**0.5))**2
    else:
        return -1

n = 3
print(solution(n))