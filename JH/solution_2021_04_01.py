def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    else:
        s_n = s // n
        for i in range(n):
            answer.append(s_n)
        sp = s % n
        
        idx = -1
        for i in range(sp):
            answer[idx-i] += 1
            
    return answer
