def solution(n, lost, reserve):
    comm = set(lost)&set(reserve)
    lost = list(set(lost)-comm)
    reserve = list(set(reserve)-comm)
    lost.sort(reverse=True)
    cnt = 0
    for l in lost:
        for ck in [l,l+1,l-1]:
            if ck in reserve:
                reserve.remove(ck)
                cnt += 1
                break
    return n-len(lost)+cnt


n = 8
lost = [5,6]
reserve = [4,5]
print(solution(n,lost,reserve))