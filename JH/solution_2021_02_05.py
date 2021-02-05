def solution(people, limit):
    answer = 0
    people = sorted(people)
    # 정렬하여 맨뒤와 맨 앞을 비교한다.
    success = []
    i = 0
    j = len(people) - 1
    while i <= j:
        a = people[i]
        b = people[j]
        # 어차피 최대 2명이니 2값만 비교
        if a + b <= limit:
            i += 1
        # limit보다 작으면 태울수 있으니 i 값 한번 증가
        j = j - 1
        # 태웠어도 감소 못태웠으면 j값 감소해서 그 다음꺼 찾기
        answer += 1
        # 보트 태웠으니 증가
        
        
    return answer