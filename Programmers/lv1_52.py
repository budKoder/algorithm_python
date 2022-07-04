def solution(phone_number):
    return '*' * (len(phone_number)-4) + phone_number[-4:]

phone_number = '027778888'
print(solution(phone_number))