def solution(prices):
    # 효율성 통과
    answer = []
    a = []
    # 스택에 넣을 배열 선언
    count = 0
    for i in range(len(prices)):
        number = prices[i]
        for j in range(i+1,len(prices)):
            # 시점으로부터 값을 비교 
            number2 = prices[j]
            if number2 >= number:
            # 스택 푸시
                a.append(number2)
            else:
            # 마지막이라도 그 순간이지만 값이 오르지 않았기떄문에 스택에 푸시
                a.append(number2)
                break
        answer.append(len(a))
        # 스택길이만큼 answer 배열에 푸쉬
        a = []
    return answer
