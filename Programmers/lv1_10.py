def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        n1 = nums[i]
        for j in range(i+1,len(nums)-1):
            n2 = nums[j]
            for k in range(j+1,len(nums)):
                n3 = nums[k]
                if isPrime(n1+n2+n3):
                    answer+=1
    return answer


nums = [1,2,7,6,4]
print(solution(nums))