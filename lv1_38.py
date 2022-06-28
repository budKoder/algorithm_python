def solution(s):
    if s[0] in ['-','+']:
        return int(s[1:])*(-1) if s[0] == '-' else int(s[1:])
    else:
        return int(s)