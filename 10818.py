import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
print(f"{min(arr)} {max(arr)}")