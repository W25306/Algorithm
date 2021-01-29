def solution(n, arr1, arr2):
    answer = []
    arr1_sh = []
    arr2_sh = []
    for i in arr1:
        temp = []
        for j in range(i):
            mod = i % 2
            s = i // 2
            i = s
            if s == 1:
                temp.append(mod)
                temp.append(s)
                break
            else:
                temp.append(mod)
        temp.reverse()
        if len(temp) < n:
            a = n - len(temp)
            for j in range(a):
                temp.insert(0,0)
        arr1_sh.append(temp)
    for i in arr2:
        temp = []
        for j in range(i):
            mod = i % 2
            s = i // 2
            i = s
            if s == 1:
                temp.append(mod)
                temp.append(s)
                break
            else:
                temp.append(mod)
        temp.reverse()
        
        if len(temp) < n:
            a = n - len(temp)
            for j in range(a):
                temp.insert(0,0)
        arr2_sh.append(temp)
    
    for i in range(n):
        answers = ''
        for j in range(n):
            if arr1_sh[i][j] == 1 or arr2_sh[i][j] == 1:
                answers += '#'
            else:
                answers += ' '
        answer.append(answers)         
    
    return answer

import math

def solution(dartResult):
    a = []
    n = 0
    
    for i in range(n,len(dartResult)-1):
        if dartResult[i].isdigit() and dartResult[i+1].isdigit():
            a.append([i,i+1])
            n += 2
        elif dartResult[i].isdigit() and not dartResult[i+1].isdigit():
            a.append([i])
            n = n + 1
    remove_index = []
    for i in range(len(a)):
        if len(a[i]) == 2:
            remove_index.append(i+1)
    for i in range(len(remove_index)):
        a.pop(remove_index[i]-i)
                
    first = dartResult[a[0][0]:a[1][0]]
    second = dartResult[a[1][0]:a[2][0]]
    third = dartResult[a[2][0]:]
    first_score = 0
    second_score = 0
    third_score = 0
        
    for i,st in enumerate(first):
        if i == 0 and first[i+1].isdigit():
            first_score = 10
        elif i == 0 and not first[i+1].isdigit():
            first_score = int(st)
        else:
            if st == 'S':
                first_score = math.pow(first_score,1)
            elif st == 'D':
                first_score = math.pow(first_score,2)
            elif st == 'T':
                first_score = math.pow(first_score,3)
            elif st == '*':
                first_score *= 2
            elif st == '#':
                first_score *= -1
            else:
                continue
                
    for i,st in enumerate(second):
        if i == 0 and second[i+1].isdigit():
            second_score = 10
        elif i == 0 and not second[i+1].isdigit():
            second_score = int(st)
        else:
            if st == 'S':
                second_score = math.pow(second_score,1)
            elif st == 'D':
                second_score = math.pow(second_score,2)
            elif st == 'T':
                second_score = math.pow(second_score,3)
            elif st == '*':
                second_score *= 2
                first_score *= 2
            elif st == '#':
                second_score *= -1
            else:
                continue
                
    for i,st in enumerate(third):
        if i == 0 and third[i+1].isdigit():
            third_score = 10
        elif i == 0 and not third[i+1].isdigit():
            third_score = int(st)      
        else:
            if st == 'S':
                third_score = math.pow(third_score,1)
            elif st == 'D':
                third_score = math.pow(third_score,2)
            elif st == 'T':
                third_score = math.pow(third_score,3)
            elif st == '*':
                second_score *= 2
                third_score *= 2
            elif st == '#':
                third_score *= -1
            else:
                continue           
    return int((first_score+ second_score +third_score))    