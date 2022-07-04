import math
def solution(w,h):
    fragment = math.ceil(h/w)
    return w*h - (w*fragment)


w = 3
h = 1523730
print(solution(w,h))