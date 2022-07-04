def solution(s,n):
    answer = ''
    for x in s:
        if not x.isalpha():
            answer += x
        else:
            o = ord(x) + n
            if (ord(x) < 91 and o > 90) or (ord(x) < 123 and o > 122):
                o -= 26
            answer += chr(o)
    return answer

s = 'z'
n = 1
print(ord('z'))
print(ord('Z'))
print(solution(s,n))