def solution(s):
    answer = ''
    idx = 0
    cnt = 0
    while idx < len(s):
        if not s[idx].isalpha():
            answer += s[idx]
            cnt = 0
        else:
            answer += s[idx].upper() if cnt%2 == 0 else s[idx].lower()
            cnt += 1
        idx += 1
    return answer

s = "try hello  world"
print(solution(s))