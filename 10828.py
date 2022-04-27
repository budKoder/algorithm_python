import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        print(-1 if len(stack) == 0 else stack.pop(-1))
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == "top":
        print(-1 if len(stack) == 0 else stack[-1])
