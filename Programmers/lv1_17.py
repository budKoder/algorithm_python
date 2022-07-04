def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if float.is_integer(n**0.5):
            answer -= n
        else:
            answer += n
    return answer

left = 24
right = 27
print(solution(left, right))