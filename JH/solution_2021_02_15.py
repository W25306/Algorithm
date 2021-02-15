def solution(phone_book):
    answer = True
    # 기본값 설정
    lis = list(zip(phone_book))
    # 딕셔너리 형태로
    for i,num in enumerate(lis):
        a = num[0]
        # 딕셔너리중 한 값을 가지고옴
        b = lis.copy()
        # 딕셔너리 복사
        for j,num2 in enumerate(b):
            c = len(a)
            if num2[0][:c] == a and i != j:
                #만약 앞의 글자가 같으면? 떙!
                return False
    return answer