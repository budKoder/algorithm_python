def solution(s):
    cnt1 = s.upper().count('P')
    cnt2 = s.upper().count('Y')
    return True if cnt1 == cnt2 else False