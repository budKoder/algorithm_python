import sys
s = sys.stdin.readline().strip()
rs = s[-1::-1]
if s == rs:
    print(1)
else:
    print(0)