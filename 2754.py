import sys
score = sys.stdin.readline().strip()
result = 0
if score[0] == "A":
    result = 4.3
elif score[0] == "B":
    result = 3.3
elif score[0] == "C":
    result = 2.3
elif score[0] == "D":
    result = 1.3
if score[-1] == "0":
    result -= 0.3
elif score[-1] == "-":
    result -= 0.6

print("{:.1f}".format(result))