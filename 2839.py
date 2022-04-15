import sys
n = int(sys.stdin.readline())

cnt_list = [-1 for _ in range(n)]

cnt_list[2] = 1
if n >= 5:
    cnt_list[4]=1

for i in range(5,n):
    cnt1 = cnt_list[i-3]
    cnt2 = cnt_list[i-5]

    if cnt1 != -1 and cnt2 != -1:
        cnt_list[i] = min(cnt1, cnt2)+1
    elif cnt1 != -1 and cnt2 == -1:
        cnt_list[i] = cnt1 + 1
    elif cnt1 == -1 and cnt2 != -1:
        cnt_list[i] = cnt2 + 1

print(cnt_list[-1])