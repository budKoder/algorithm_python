def solution(numbers):
    total = set([i for i in range(10)])
    numbers = set(numbers)
    return sum(total-numbers)

numbers = [5,8,4,0,6,7,9]
print(solution(numbers))