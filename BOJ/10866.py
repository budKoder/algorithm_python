if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    deq = []
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "push_front":
            deq.insert(0,cmd[1])
        elif cmd[0] == "push_back":
            deq.append(cmd[1])
        elif cmd[0] == "pop_front":
            print(deq.pop(0) if len(deq) > 0 else -1)
        elif cmd[0] == "pop_back":
            print(deq.pop(-1) if len(deq) > 0 else -1)
        elif cmd[0] == "size":
            print(len(deq))
        elif cmd[0] == "empty":
            print(1 if len(deq) == 0 else 0)
        elif cmd[0] == "front":
            print(deq[0] if len(deq) > 0 else -1)
        elif cmd[0] == "back":
            print(deq[-1] if len(deq) > 0 else -1)
