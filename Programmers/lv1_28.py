def solution(arr):
    answer = [-1]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    return answer[1:]

arr = [1,1,3,3,0,1,1]
print(solution(arr))