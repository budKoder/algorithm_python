def solution(n):
    nums = list(map(str,str(n)))
    nums.sort(reverse=True)
    return int(''.join(nums))

n =118372
print(solution(n))