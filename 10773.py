import sys
k = int(sys.stdin.readline())
st = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        st.pop(-1)
    else:
        st.append(n)
print(sum(st))