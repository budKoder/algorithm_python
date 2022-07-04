def solution(n):
    answer = 0
    for x in range(2,n):
        if (n-1)%x == 0:
            answer = x
            break
    return answer

n = 12
print(solution(n))

