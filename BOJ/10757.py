import sys
a,b = sys.stdin.readline().split()
max_length = len(a) if len(a) > len(b) else len(b)
result = 0
a = int(a)
b = int(b)
for i in range(max_length):
    result += (a%10 + b%10)*(10**i)
    a = a//10
    b = b//10
print(result)
