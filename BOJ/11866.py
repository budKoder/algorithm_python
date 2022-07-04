import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
dq = deque([str(i+1) for i in range(n)])
result = []
k *= -1
while len(dq) > 0:
    dq.rotate(k+1)
    result.append(dq.popleft())
print('<'+', '.join(result)+'>')