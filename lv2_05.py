import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    dq = deque([math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))])
    while dq:
        item = dq.popleft()
        cnt = 1
        while dq:
            if dq[0] <= item:
                dq.popleft()
                cnt+=1
            else:
                break
        answer.append(cnt)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))