import sys
_ = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())
cnt_a = s.count("A")
cnt_b = s.count('B')
if cnt_a > cnt_b:
    print("A")
elif cnt_a == cnt_b:
    print("Tie")
else:
    print("B")