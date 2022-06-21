def solution(board, moves):
    answer = 0
    st = []
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                if len(st) != 0 and st[-1] == j[i-1]:
                    st.pop(-1)
                    answer += 2
                else:
                    st.append(j[i-1])
                j[i-1] = 0
                break
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)