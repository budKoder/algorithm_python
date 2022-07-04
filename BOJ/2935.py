import sys
a = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
b = int(sys.stdin.readline())
if s == "+":
    print(a+b)
elif s == "*":
    print(a*b)