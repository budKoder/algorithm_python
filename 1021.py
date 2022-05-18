import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
dq = deque([i+1 for i in range(n)])
arr = deque(map(int,sys.stdin.readline().split()))

cnt = 0
while len(arr) > 0:
    index = dq.index(arr[0])
    if index == 0:
        dq.popleft()
        arr.popleft()
    else:
        cnt += 1
        reverse_index = len(dq) - index
        if abs(index) < abs(reverse_index):
            dq.rotate(-1)
        else:
            dq.rotate(1)
print(cnt)