def solution(board):
    answer = 0
    if len(board) == 1 and len(board[0]) == 1:
        if board[0][0] == 0:
            #가로 길이가 1인경우 0일때는 0반환
            return 0
        elif board[0][0] == 1:
            # 가로나 세로 길이가 1인 경우에 1일때는 1반환
            return 1
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                #만약 0이 아니면 위 옆 대각선 값 알아내서 최솟값 구해서 1더해버리기
                prev_row = board[i-1][j]
                prev_col = board[i][j-1]
                prev_row_col = board[i-1][j-1]
                board[i][j] = min(prev_row,prev_col,prev_row_col) + 1
            answer = max(answer, board[i][j])
            # 제곱값
    return answer ** 2
