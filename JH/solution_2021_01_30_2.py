def solution(n):
    temp = ''
    b = ['1','2','4']
    while n:
        a = (n % 3)
        
        n = n // 3
        if a % 3 == 0:
            n = n - 1
        if a == 1:
            temp = '1' + temp
        elif a == 2:
            temp = '2' + temp
        elif a == 0:
            temp = '4' + temp
    return temp
