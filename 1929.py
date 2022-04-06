def solution(start, end):
    arr = [[_,True] for _ in range(end+1)]

    for i in range(2,len(arr)):
        num = arr[i][0]
        check = arr[i][1]

        if check:
            if num >= start:
                print(num)
            uncheck = num + num
            while uncheck <= end:
                arr[uncheck][1] = False
                uncheck += num


if __name__ == "__main__":
    import sys
    m,n = map(int,sys.stdin.readline().split())
    solution(m,n)