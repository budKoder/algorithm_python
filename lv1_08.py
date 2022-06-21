def solution(absolutes, signs):
    answer = 123456789
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i] *= -1
    return sum(absolutes)

absolutes = [4,7,12]
signs = [True, False, True]
print(solution(absolutes,signs))