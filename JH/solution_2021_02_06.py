import math
def solution(progresses, speeds):
    answer = []
    a = []
    # 임시 배열 선언
    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        # 남은 퍼센트 구현
        speed = speeds[i]
        # 각 작업의 스피트
        a.append(math.ceil(rest/speed))
        # 남은 값을 통해서 올림처리한다 왜? => 70 , 30 이라고 한다고하면 3일은 걸림 2.1일등은 존재하지 않음
    i = 0
    # 인덱스값 선언
    for j in range(len(a)):
        if i == len(a):
            break
        # i가 다돌아버렸다면..?
        else:
            idx = a[i]
            # 값하나 가지고온다
            count = 1
            # 최소 카운트 수 1 선언
            for k in range(i+1,len(a)):
                if idx >=a[k]:
                    # 만약 다음 작업이 더 빨리 끝났으면 한번에 배포해버려야하니 증가
                    count += 1
                    i = k
                else:
                    break
            i+= 1
            # 다음 작업으로 넘어가서
            answer.append(count)
            # 배포 카운트 답에 추가
        
    return answer
