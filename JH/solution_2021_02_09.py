import math
def solution(n):
    answer = 0
    a = []
    s = n
    count = 0
    # 이진수 변환
    while s > 0 :
        mod = s % 2
        s = s//2
        a.append(mod)
        if mod == 1:
            count += 1
    # 1의 갯수를 세기
    while True:
        n += 1
        # 1값 증가시켜서
        s = n
        count2 = 0
        # 반복문을 돈 다음 count가 같으면 반환
        while s > 0 :
            mod = s % 2
            s = s//2
            if mod == 1:
                count2 += 1
        if count2 == count:
            answer = n
            break
    return answer