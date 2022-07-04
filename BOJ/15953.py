import sys

n = int(sys.stdin.readline())

first_fes = [1, 3, 6, 10, 15, 21]
first_prize = [500, 300, 200, 50, 30, 10]
second_fes = [1, 3, 7, 15, 31]
second_prize = [512, 256, 128, 64, 32]

for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    total = 0
    for i in range(len(first_fes)):
        if a>21 or a==0:
            break
        elif a<=first_fes[i]:
            total+=first_prize[i]
            break
    for j in range(len(second_fes)):
        if b>31 or b==0:
            break
        elif b <=second_fes[j]:
            total+=second_prize[j]
            break
    print(total*10000)

