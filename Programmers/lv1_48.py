def divisor(n):
    d = set()
    for i in range(1,n+1):
        if n%i == 0:
            d.add(i)
    return d


def solution(n, m):
    dn = divisor(n)
    dm = divisor(m)
    gcd = max(dn & dm)
    lcm = n * m // gcd
    return [gcd, lcm]


n = 2
m = 5
print(solution(n,m))