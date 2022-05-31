import sys
s = sys.stdin.readline().strip()
h = 10
for i in range(1,len(s)):
    if s[i-1] != s[i]:
        h += 10
    else:
        h += 5
print(h)