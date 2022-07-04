def solution(n):
    answer = 0
    s = ''
    while n>0:
        s += str(n%3)
        n //= 3
    print(s)
    for i in range(len(s)-1, -1, -1):
        answer += pow(3,len(s)-1-i) * int(s[i])
    return answer

n = 125
print(solution(n))