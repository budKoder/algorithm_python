def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('')
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]



participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant,completion))