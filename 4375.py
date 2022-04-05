def solution(n):
    i = 1
    num = 1
    while True:
        if num % n != 0:
            num += pow(10,i)
            i += 1
        else:
            return i


if __name__ == "__main__":
    while True:
        try:
            n = int(input())
        except:
            break

        print(solution(n))