import sys
n = int(sys.stdin.readline().strip())
cnt = 0
for i in range(1,n+1):
    if i < 100:
       cnt += 1
    else:
        i = str(i)
        chk = int(i[0])-int(i[1])
        isTarget = True
        for j in range(1,len(i)-1):
            if chk != int(i[j])-int(i[j+1]):
                isTarget=False
                break
        if isTarget:
            cnt+=1
print(cnt)