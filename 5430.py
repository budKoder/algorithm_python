import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().strip().strip('[]').split(',')

    if n == 0:
        dq = deque([])
    else:
        dq = deque(x)

    r_cnt = 0
    flag = True
    for cmd in p:
        if cmd == 'R':
            r_cnt += 1
        elif cmd == 'D':
            if len(dq) == 0:
               flag = False
               print("error")
               break
            else:
                dq.popleft() if r_cnt%2 == 0 else dq.pop()
    if flag:
        if r_cnt % 2 != 0:
            dq.reverse()
        print("["+",".join(dq)+"]")