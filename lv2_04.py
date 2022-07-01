def solution(n):
    answer = ''
    matched = {1:'1',2:'2',0:'4'}
    while n > 0:
        answer += matched[n%3]
        n = (n-1)//3
    return answer[::-1]

for i in range(1,11):
    print(solution(i))