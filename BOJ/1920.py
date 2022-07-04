import sys


def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid-1
        else:
            low = mid + 1
    return -1


n = int(sys.stdin.readline())
nList = list(map(int,sys.stdin.readline().split()))
nList.sort()
m = int(sys.stdin.readline())
mList = list(map(int,sys.stdin.readline().split()))
for item in mList:
    if binary_search(nList,item) == -1:
        print(0)
    else:
        print(1)
