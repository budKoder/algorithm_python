def solution(lottos, win_nums):
    answer = []

    zero_cnt = lottos.count(0)
    min_num = len(set(lottos) & set(win_nums))
    max_num = min_num+zero_cnt

    for num in [max_num, min_num]:
        result = 6
        if num == 6:
            result = 1
        elif num == 5:
            result = 2
        elif num == 4:
            result = 3
        elif num == 3:
            result = 4
        elif num == 2:
            result = 5
        answer.append(result)
    return answer


lottos = [45, 4, 35, 20, 3, 9]
win_nums = 	[20, 9, 3, 45, 4, 35]
print(solution(lottos,win_nums))