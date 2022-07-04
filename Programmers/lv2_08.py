def rotate(sRow, sCol, eRow, eCol, arr):
    prev = arr[sRow][sCol]
    rotated = [prev]
    for i in range(sCol+1, eCol+1):
        prev, arr[sRow][i] = arr[sRow][i], prev
        rotated.append(prev)
    for i in range(sRow+1, eRow+1):
        prev, arr[i][eCol] = arr[i][eCol], prev
        rotated.append(prev)
    for i in range(eCol-1, sCol-1, -1):
        prev, arr[eRow][i] = arr[eRow][i], prev
        rotated.append(prev)
    for i in range(eRow-1, sRow-1, -1):
        prev, arr[i][sCol] = arr[i][sCol], prev
        rotated.append(prev)
    rotated.sort()
    return rotated[0]


def solution(rows, columns, queries):
    answer = []
    arr = [[i*columns + j+1 for j in range(columns)] for i in range(rows)]
    for sRow, sCol, eRow, eCol in queries:
        minNum = rotate(sRow-1, sCol-1, eRow-1, eCol-1, arr)
        answer.append(minNum)
    return answer

rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))