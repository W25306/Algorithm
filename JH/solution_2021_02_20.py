def solution(clothes):
    answer = 1
    b = []   
    a = []
    for i in clothes:
        b.append(i[1])
    b = list(set(b))
    for i in range(len(b)):
        a.append([b[i],0])

    for i in clothes:
        s = i[1]
        for j in range(len(a)):
            if s == a[j][0]:
                a[j][1] += 1
    if len(b) == 1:
        return len(clothes)
    else:
        for i in range(len(a)):
            
            answer *= (a[i][1] + 1)
        
    return answer - 1
