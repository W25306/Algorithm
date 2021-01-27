def solution(s):
    answer = ''
    array = s.split(' ')
    answers = []
    print(array)
    for i in array:
        temp = ''
        for j in range(len(i)):
            if j % 2 == 0:
                temp += i[j].upper()
            elif j % 2 == 1:
                temp += i[j].lower()
        answers.append(temp)
    
    return ' '.join(answers)

def solution(s, n):
    s = list(s) 
    for i in range(len(s)): 
        if s[i].isupper(): 
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A')) 
        elif s[i].islower(): s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a')) 
    return "".join(s)

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    r = ['.','-','_']
    for i in range(len(new_id)):
        if new_id[i].islower() or new_id[i].isdigit() or new_id[i] in r:
            pass
        else:
            new_id = new_id.replace(new_id[i],"^")
    new_id = new_id.replace('^',"")
    # 3단계
    b = []
    for i in range(0,len(new_id)):
        if i == 0 and new_id[i] == '.':
            b.append(new_id[i])
        elif new_id[i] == '.' and new_id[i-1] == '.':
            continue
        else:
            b.append(new_id[i])
    #4단계
    if b[0] == '.' and len(b) > 0:
        b.pop(0)
    if len(b) >0:
        if b[-1] == '.':
            b.pop(-1)
    
    
    #5단계
    if len(b) == 0:
        b = ['a','a','a']
    #6단계
    if len(b) > 15:
        b = b[:15]
        if b[14] == '.':
            b.pop(14)
    #7단계
    if len(b) < 3:
       while len(b) != 3:
            b.append(b[-1])
            
    for i in range(len(b)):
        answer += b[i]
    return answer    