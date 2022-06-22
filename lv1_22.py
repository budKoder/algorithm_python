def solution(sizes):
    sizes = [sorted(s) for s in sizes]
    return max(s[0] for s in sizes) * max(s[1] for s in sizes)

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))