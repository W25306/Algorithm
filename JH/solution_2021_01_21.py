def solution(board, moves):
    backet = []
    answer = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] != 0:
                backet.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break
        if len(backet) == 0 or len(backet) == 1:
            continue
        else:
            if backet[-1] == backet[-2]:
                del backet[-1]
                del backet[-1]
                answer += 2
    return answer