def solution(N, stages):
    answer = []
    for i in range(1,N+1):
        current = stages.count(i)
        success = sum(1 for j in stages if j>=i)
        answer.append([i, 0 if success == 0 else current/success])
    answer.sort(key=lambda x:x[1], reverse=True)
    return [a[0] for a in answer]

N = 4
stages = 	[4,4,4,4,4]
print(solution(N, stages))