import sys


def binSearch(arr, num):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == num:
            return 1
        elif arr[mid] > num:
            high= mid - 1
        elif arr[mid] < num:
            low = mid + 1
    return 0


n = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
for n in nums:
    print(binSearch(cards,n), end=' ')
