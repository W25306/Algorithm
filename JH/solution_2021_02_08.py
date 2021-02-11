def solution(s):
    a = []
    # 스택배열 선언
    for i in s:
        if len(a) == 0:
            # 초기에 배열 넣기
            a.append(i)
        elif a[-1] == i:
            # 같으면 pop
            a.pop()
        elif a[-1] != i:
            # 다르면 추가
            a.append(i)
    if len(a) == 0:
        return 1
    else:
        return 0
    
