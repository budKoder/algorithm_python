def pack(s, cnt):
    answer = ''

    start = 0
    end = start + cnt
    word = s[start:end]
    num = 1

    while end < len(s):
        start += cnt
        end += cnt
        if s[start:end] == word:
            num += 1
            word = s[start:end]
        else:
            answer += "{}{}".format(num,word) if num > 1 else "{}".format(word)
            word = s[start:end]
            num = 1
    answer += "{}{}".format(num,word) if num > 1 else "{}".format(word)
    return answer


def solution(s):
    length = len(s)
    for i in range(1,len(s)+1):
        packed = pack(s,i)
        if len(packed) < length:
            length = len(packed)
    return length

s ="xababcdcdababcdcd"
print(solution(s))