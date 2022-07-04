import sys
n = int(sys.stdin.readline())
nList = []
for _ in range(n):
    ns = list(map(int,sys.stdin.readline().split()))
    nList.append(ns)

for i in range(n-2, -1, -1):
    for j in range(len(nList[i])):
        n1 = nList[i][j] + nList[i+1][j]
        n2 = nList[i][j] + nList[i+1][j+1]
        nList[i][j] = max(n1,n2)

print(nList[0][0])