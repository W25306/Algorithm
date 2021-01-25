import math

def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

def solution(n):
    answer = 0
    three_answer = []
    while(n >= 1):
        number = n % 3
        three_answer.insert(0,number)
        n = n // 3
    
    reverse_answer = []
    for i in range(len(three_answer)):
        reverse_answer.append(three_answer[-(i + 1)])
        
    print(reverse_answer)
    for i in range(len(three_answer)):
        pow = math.pow(3,i)
        answer += reverse_answer[-(i + 1)] * pow
        
    return answer

def solution(s):
    text_length = len(s)
    if text_length % 2 == 0:
        answer = s[text_length // 2 -1: text_length // 2 + 1]
    else:
        answer = s[text_length // 2]
    
    return answer

def solution(arr):
    answer=[]
    i = 0
    for index in range(len(arr)):
        if i > len(arr):
            break
        else:
            number = arr[i]
            for j in range(i,len(arr)):
                if arr[j] != number:
                    i = j
                    answer.append(number)
                    break
                elif number == arr[j] and j == len(arr) - 1:
                    i = len(arr) + 1
                    answer.append(arr[j])
                    break
        
    return answer    