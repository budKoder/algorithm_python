def solution(answers):
    answer = []
    sols = {
        1:[1,2,3,4,5],
        2:[2,1,2,3,2,4,2,5],
        3:[3,3,1,1,2,2,4,4,5,5]
    }
    result = []
    for name, sol in sols.items():
        cnt = 0
        for i in range(len(answers)):
            if answers[i] == sol[i%len(sol)]:
                cnt += 1
        result.append(cnt)
    for idx, values in enumerate(result):
        if values == max(result):
            answer.append(idx+1)
    return answer

answer = [1,3,2,4,2]
print(solution(answer))