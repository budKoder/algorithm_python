def solution(s):
    answer = [s[0]]
    for i in range(1,len(s)):
        if len(answer) == 0 or answer[-1] != s[i]:
            answer.append(s[i])
        else:
            answer.pop()
    if len(answer) == 0:
        return 1
    else:
        return 0

s = "cdcd"
print(solution(s))