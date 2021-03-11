def solution(citations):
    answer = 0
    a = sorted(citations)
    n = len(citations)
    h = 0
    for i in range(max(a)+1):
        t = i
        # count = 인용논문
        count = 0
        for j in range(n):
            if t <= a[j]:
                count += 1
        if i <= n and count >= i:
            h = i
    return h
