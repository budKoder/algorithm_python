import sys
result = set()
for _ in range(10):
    num = int(sys.stdin.readline())
    result.add(num%42)
print(len(result))