def solution(numbers):
    answer = ''
    a = []
    for i in range(len(numbers)):
        num = str(numbers[i])
        a.append([num,num])
    for i in range(len(a)):
        sel_num = a[i]
        for j in range(2):
            sel_num[0] += str(numbers[i])
    a = sorted(a,reverse=True)
    for i in range(len(a)):
        if a[0][1] == '0':
            return '0'
        else:
            answer += a[i][1]
    return answer