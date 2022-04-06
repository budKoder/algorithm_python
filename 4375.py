def solution(n):
    num = 0
    i = 1
    while True:
        num = num * 10 + 1
        num %= n
        if num == 0:
            return i
        i+=1


if __name__ == "__main__":
    while True:
        try:
            n = int(input())
        except:
            break

        print(solution(n))