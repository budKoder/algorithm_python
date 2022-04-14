nums = set(range(1,10001))
d_nums = set()
for i in range(1,10001):
    isum = sum(list(map(int,str(i))))
    d_nums.add(i+isum)

self_num = sorted(nums - d_nums)
for num in self_num:
    print(num)