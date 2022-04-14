import sys
n,m=map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(str,sys.stdin.readline().strip())))

start_point = []
for x in range(n-7):
    for y in range(m-7):
        start_point.append((x,y))

result = n*m
for x,y in start_point:
    w_cnt = 0
    b_cnt = 0
    for i in range(8):
        for j in range(8):
            """
            맨 왼쪽 위칸이 흰색(W)인 경우
            1) i/j가 짝/짝 또는 홀/홀이면 W
            2) i/j가 짝/홀 또는 홀/짝이면 B
            """
            if (i+j)%2 == 0:
                if arr[x+i][y+j] != "W":
                    w_cnt += 1
                else:
                    b_cnt += 1
            else:
                if arr[x+i][y+j] != "B":
                    w_cnt += 1
                else:
                    b_cnt += 1
    if result > min(w_cnt,b_cnt):
        result = min(w_cnt,b_cnt)
print(result)