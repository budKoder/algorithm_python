import sys


def getUpperBound(arr,n):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low+high)//2
        if arr[mid] <= n:
            low = mid+1
        else:
            high = mid
    return high


def getLowerBound(arr,n):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low+high)//2
        if arr[mid]>=n:
            high = mid
        else:
            low = mid+1
    return high


n = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
for l in li:
    upper_bound = getUpperBound(cards,l)
    lower_bound = getLowerBound(cards,l)
    print(upper_bound - lower_bound, end=' ')