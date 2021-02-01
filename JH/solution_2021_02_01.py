def solution(priorities, location):
    a = []
    for i,p in enumerate(priorities):
        a.append([i,p])
    # 새로운 배열 정의 => 인덱스, 
    lis = sorted(priorities)
    # 우선순위 정렬 마지막이 가장 우선순위가 높게
    answer = 0
    b = []
    # 우선순위에 맞게 프린터 순서에 넣을 배열 선언
    i = 0
    # 만약 길이가 1이라면 1리턴
    if len(priorities) == 1:
        return 1
    else:
        # 우선순위에 맞게 넣을 배열의 길이가 우선순위 배열의 길이와 같을때 까지 반복
        while len(b) < len(priorities):
            s = a[i]
            # 한개의 값을 가지고온다.
            if s[1] == lis[-1]:
                b.append(s)
                a.pop(0)
                lis.pop(-1)
                i = 0
                # 만약 처음에 값이 가장 우선순위가 높다면 배열에 추가하고 a,lis 배열 팝 이제 의미없기 때문 다시 i 를 0으로
            else:
                # 아니라면 반복문 돌아서
                for j in range(1,len(priorities)):
                    # 만일 우선순위가 낮다면
                    if s[1] < max(lis):
                        # 배열 마지막에 추가
                        a.append(s)
                        # 원래 자리 pop
                        a.pop(i)
                        i -=1
                        #i값 감소
                        break
                i += 1
    # location을 통해서 일치하는 값의 위치를 찾아 1더해 반환
    for i in range(len(b)):
        if location == b[i][0]:
            answer = i + 1
            
    return answer