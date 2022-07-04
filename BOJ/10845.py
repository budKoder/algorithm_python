if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "pop":
            print(arr.pop(0) if len(arr) > 0 else -1)
        elif cmd[0] == "size":
            print(len(arr))
        elif cmd[0] == "empty":
            print(1 if len(arr) == 0 else 0)
        elif cmd[0] == "front":
            print(arr[0] if len(arr) > 0 else -1)
        elif cmd[0] == "back":
            print(arr[-1] if len(arr) > 0 else -1)
        elif cmd[0] == "push":
            arr.append(cmd[1])