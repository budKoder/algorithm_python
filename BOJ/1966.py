import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    dq = deque(list(map(int,sys.stdin.readline().split())))
    cnt = 0
    while len(dq) > 0:
        prior = max(dq)
        front = dq.popleft()
        if m == 0:
            if front == prior:
                cnt += 1
                break
            else:
                m = len(dq)
                dq.append(front)
        else:
            m -= 1
            if front == prior:
                cnt += 1
            else:
                dq.append(front)
    print(cnt)