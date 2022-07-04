def solution(price, money, count):
    required = price * count * (count + 1) // 2
    return 0 if money >= required else required - money

price = 3
money = 20
count = 4
print(solution(price,money,count))