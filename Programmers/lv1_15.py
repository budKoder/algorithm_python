def solution(nums):
    answer = 0
    s = set(nums)
    if len(s) >= len(nums)/2:
        answer = int(len(nums)/2)
    else:
        answer = len(s)
    return answer

nums =[3,3,3,2,2,4]
print(solution(nums))