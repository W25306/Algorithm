def solution(s):
    text_length = len(s)
    if text_length % 2 == 0:
        answer = s[text_length // 2 -1: text_length // 2 + 1]
    else:
        answer = s[text_length // 2]
    
    return answer

def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
        
    return answer

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer = sorted(answer)
    return answer

def solution(a, b):
    min_val = min(a,b)
    length = max(a,b) - min_val
    answer = min_val
    for i in range(length):
        answer += min_val + 1
        min_val += 1
    return answer

def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings = sorted(strings)
    print(strings)
    for i in range(len(strings)):
        answer.append(strings[i][1:])
    return answer