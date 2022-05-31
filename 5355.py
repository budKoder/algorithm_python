import sys
t = int(sys.stdin.readline())
for _ in range(t):
    arr = list(sys.stdin.readline().strip().split())
    n = float(arr[0])
    for i in range(1,len(arr)):
        s = arr[i]
        if s == "@":
            n *= 3
        elif s == "%":
            n += 5
        elif s == "#":
            n -= 7
    print("{:.2f}".format(n))