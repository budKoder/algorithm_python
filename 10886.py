import sys
n = int(sys.stdin.readline())
cnt0 = 0
cnt1= 0
for _ in range(n):
    if int(sys.stdin.readline()) == 0:
        cnt0+=1
    else:
        cnt1+=1
if cnt0>cnt1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")