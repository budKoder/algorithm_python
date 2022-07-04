def solution(id_list, report, k):
    answer = []
    send = dict()
    received = dict()
    for id in id_list:
        send[id] = set()
        received[id] = set()
    for r in report:
        sender, receiver = r.split()
        send[sender].add(receiver)
        received[receiver].add(sender)

    over = set()
    for key,val in received.items():
        if len(val) >= k:
            over.add(key)

    for key,val in send.items():
        num = len(over & val)
        answer.append(num)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(id_list, report, k)