def solution(s):
    '중간 수 더하기'
    text_length = len(s)
    if text_length % 2 == 0:
        answer = s[text_length // 2 -1: text_length // 2 + 1]
    else:
        answer = s[text_length // 2]
    
    return answer

def solution(arr):
    '같은 숫자는 싫어'
    a = []
    for i in arr:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
        
    return answer

def solution(arr, divisor):
    '나누기 가능한 수 정렬'
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer = sorted(answer)
    return answer

def solution(a, b):
    '두 수 사이의 합 더하기'
    min_val = min(a,b)
    length = max(a,b) - min_val
    answer = min_val
    for i in range(length):
        answer += min_val + 1
        min_val += 1
    return answer

def solution(strings, n):
    '문자열 
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings = sorted(strings)
    print(strings)
    for i in range(len(strings)):
        answer.append(strings[i][1:])
    return answer
