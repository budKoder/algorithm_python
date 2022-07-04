def solution(dartResult):
    i = 0
    nums = [0]
    while i < len(dartResult):
        if dartResult[i].isdigit():
            n = dartResult[i]
            if dartResult[i+1].isdigit():
                i+=1
                n+=dartResult[i]
            nums.append(int(n))
        elif dartResult[i] in ['D','T']:
            nums[-1] = pow(nums[-1],2 if dartResult[i] == 'D' else 3)
        elif dartResult[i] == '*':
            nums[-1] *= 2
            nums[-2] *= 2
        elif dartResult[i] == '#':
            nums[-1] *= -1
        i+=1
    return sum(nums)


dartResult = '1S2D*3T'
print(solution(dartResult))