import sys
n = int(sys.stdin.readline())
pi_list = list(map(int,sys.stdin.readline().split()))
pi_list.sort()
time = 0
for i in range(n):
    time += (n-i)*pi_list[i]
print(time)