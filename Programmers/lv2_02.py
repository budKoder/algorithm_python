def solution(record):
    id = dict()
    for r in record:
        txt = r.split()
        if len(txt) > 2:
            id[txt[1]] = txt[2]
    answer = []
    for r in record:
        txt = r.split()
        if txt[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(id[txt[1]]))
        elif txt[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(id[txt[1]]))
    return answer


records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records))