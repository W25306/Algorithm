def solution(w,h):
    answer = 0
    def recursive(n,c):
        if c == 0:
            return n
        else:
            return recursive(c,n%c)
    f = recursive(w,h)
    answer = w*h - (w + h - f)
    return answer
