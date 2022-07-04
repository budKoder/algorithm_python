from collections import deque
import sys

n = int(sys.stdin.readline())
dq = deque([_ for _ in range(1,n+1)])

while len(dq) > 1:
    dq.popleft()
    n = dq.popleft()
    dq.append(n)
print(dq[0])