import sys


def solution(arr):
    for x in range(len(arr)-1):
        for y in range(x+1,len(arr)):
            if sum(arr) - (arr[x] + arr[y]) == 100:
                del arr[y]
                del arr[x]
                return arr


if __name__ == "__main__":
    arr = [int(sys.stdin.readline().strip()) for _ in range(9)]
    arr.sort()
    result = solution(arr)
    for num in result:
        print(num)