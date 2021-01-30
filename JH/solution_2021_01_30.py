import math
def solution(name):
    answer = 0
    name = list(name)
    shouldChange = 0
    for n in name:
        if n != 'A':
            shouldChange += 1
    if not shouldChange:
        return 0
    goLeft = 0
    goRight = 0
    index = 0
    while 1:
        if name[index] != 'A':
            answer += min(ord('Z') - ord(name[index]) + 1, ord(name[index]) - ord('A'))
            name[index] = 'A'
            shouldChange -= 1
        # A가 아니면 가장 가까운 카운팅을 세고 변할 수 감서
        if not shouldChange:
            break
        # 0이면 정지
        goLeft = goRight = index
        move = 0
        # 움직이게 하기 위해서
        while 1:
            goRight += 1
            #오른쪽으로 시작한다.
            goLeft -= 1
            #왼쪽으로 시작한다.
            move += 1
            #움직이기 시작!
            if goLeft < 0:
                goLeft = len(name) - 1
            #역순방식
            if goRight > len(name) - 1:
                goRight = 0
            #정방향식    
            if name[goRight] != 'A':
                answer += move
                index = goRight
                break
            # A 안만날때 까지 반복하다 변경되여야 할 값이면 중지
            elif name[goLeft] != 'A':
                answer += move
                index = goLeft
                break
    return answer
