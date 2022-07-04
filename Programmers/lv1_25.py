def make_binary(n, num):
    s = ''
    while num > 0:
        s += str(num%2)
        num //= 2
    s = s[::-1].zfill(n)
    return list(s)


def solution(n, arr1, arr2):
    answer = []
    arr1 = [make_binary(n,i) for i in arr1]
    arr2 = [make_binary(n,i) for i in arr2]
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))