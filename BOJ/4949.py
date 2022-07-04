while True:
    sentence = input()
    if sentence == ".":
        break

    bracket = []
    flag = True

    for s in sentence:
        if s in ["(","["]:
            bracket.append(s)
        elif s == ")":
            if len(bracket) == 0 or bracket[-1] != "(":
                flag = False
                break
            else:
                bracket.pop(-1)
        elif s == "]":
            if len(bracket) == 0 or bracket[-1] != "[":
                flag = False
                break
            else:
                bracket.pop(-1)
    if len(bracket) != 0 or not flag:
        print("no")
    else:
        print("yes")