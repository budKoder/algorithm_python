import sys
arr = list(map(int,sys.stdin.readline().split()))
arr.sort(reverse=True)
print(arr[1])