def solution(arr1, arr2):
    return [[sum([arr1[i][j], arr2[i][j]]) for j in range(len(arr1[i]))] for i in range(len(arr1))]

arr1= [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))