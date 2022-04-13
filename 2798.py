import sys
n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

max = 0
for p in range(len(nums)-2):
    np = nums[p]
    for q in range(p+1,len(nums)-1):
        nq = nums[q]
        for r in range(q+1,len(nums)):
            nr = nums[r]
            sum = np+nq+nr
            if sum <= m and sum > max:
                max = sum
print(max)