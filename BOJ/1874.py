import sys
n = int(sys.stdin.readline())
st = []
cur_num = 1
result = []
flag = True
for _ in range(n):
    m = int(sys.stdin.readline())
    while cur_num <= m:
        st.append(cur_num)
        cur_num+=1
        result.append("+")

    if st[-1] == m:
        st.pop(-1)
        result.append("-")
    else:
        flag = False
        break

if flag:
    for r in result:
        print(r)
else:
    print("NO")
