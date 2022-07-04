import sys

s = list(sys.stdin.readline().strip())
idx = len(s)
m = int(sys.stdin.readline())
for _ in range(m):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "P":
        s.insert(idx,cmd[1])
        idx += 1
    elif cmd[0] == "B":
        if idx != 0:
            idx -= 1
            del s[idx]
    elif cmd[0] == "L":
        if idx != 0:
            idx -= 1
    elif cmd[0] == "D":
        if idx != len(s):
            idx += 1
print(''.join(s))