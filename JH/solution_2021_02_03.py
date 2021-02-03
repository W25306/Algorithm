def solution(n):
    res = [[0] * n for _ in range(n)]
    # n 길이 만큼 2차원 배열 생성
    answer = []
    x, y = -1, 0
    # 첫번째 값은 0,0이기때문에 1개 추가해서 0,0만들예정
    num = 1
    # 1부터 값이 들어감
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            # 만약 1번째라면 아래로 추가하기
            elif i % 3 == 1:
                y += 1
            # 나머지가 1이면 왼쪽으로
            elif i % 3 == 2:
                x -= 1
                y -= 1
            # 나머지가 2면 위칸 대각선
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer