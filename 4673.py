nums = set(range(1,10001))
d_nums = set()
for i in range(1,10001):
    num = i
    for n in str(i):
        num += int(n)
    d_nums.add(num)

self_num = sorted(nums - d_nums)
for num in self_num:
    print(num)