def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = 0
        iter1 = 0
        iter2 = 1
        for i in range(2,n+1):
            result = iter1 + iter2
            iter1 = iter2
            iter2 = result
        return result % 1234567
    return 0