def solution(arr, divisor):
    result = sorted(list(filter(lambda x : x % divisor == 0, arr)))
    return [-1] if len(result) == 0 else result

arr = [5,9,7,10]
divisor = 5
print(solution(arr,5))
