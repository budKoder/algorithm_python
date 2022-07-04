def solution(d, budget):
    d.sort()
    cnt = 0
    for price in d:
        if price <= budget:
            cnt += 1
            budget -= price
        else:
            break
    return cnt

d = [2,2,3,3]
budget = 10
print(solution(d,budget))