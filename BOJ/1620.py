import sys
n,m = map(int,sys.stdin.readline().split())
num_name = {}
name_num = {}
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    num_name[i] = name
    name_num[name] = i
for _ in range(m):
    s = sys.stdin.readline().strip()
    if s.isnumeric():
        print(num_name.get(int(s)))
    else:
        print(name_num.get(s))