def getDistance(loc, to_loc):
    return abs(to_loc[0]-loc[0]) + abs(to_loc[1]-loc[1])

def solution(numbers, hand):
    loc = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        0:(3,1)
    }
    right = (3,0)
    left = (3,2)

    answer = ''
    for n in numbers:
        if n in [1,4,7]:
            left = loc[n]
            answer += 'L'
        elif n in [3,6,9]:
            right = loc[n]
            answer += 'R'
        else:
            dr = getDistance(right, loc[n])
            dl = getDistance(left, loc[n])
            if dr < dl:
                right = loc[n]
                answer += 'R'
            elif dr > dl:
                left = loc[n]
                answer += 'L'
            else:
                if hand == "right":
                    right = loc[n]
                    answer += 'R'
                else:
                    left = loc[n]
                    answer += 'L'
    return answer

numbers =[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers,hand))