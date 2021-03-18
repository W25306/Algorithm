def solution(n, t, m, p):
    number = m
    answer = ''
    total_length = t * m
    i = 1
    c = '0'
    temp = []
    while len(c) < total_length:
        test = i
        while test != 0:
            s = test // n
            m = test % n
            if m == 10:
                m = 'A'
            elif m == 11:
                m = 'B'
            elif m == 12:
                m = 'C'
            elif m == 13:
                m = 'D'
            elif m == 14:
                m = 'E'
            elif m == 15:
                m = 'F'
            temp.append(str(m))
            test = test // n
        temp.reverse()
        g = "".join(temp)
        temp = []
        c += g
        i += 1
    c = c[:total_length]
    for j in range(p-1,len(c),number):
        answer += str(c[j])
    return answer
