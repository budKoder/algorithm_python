import sys

x_list = []
y_list = []
for _ in range(3):
    x,y = map(int,sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)
result = []
for x in x_list:
    if x_list.count(x) == 1:
        result.append(x)
        break
for y in y_list:
    if y_list.count(y) == 1:
        result.append(y)
        break
for n in result:
    print(n,end=' ')