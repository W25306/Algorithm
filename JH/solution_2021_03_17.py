def solution(s):
    answer = True
    stack = []
    if s[0] == ')' or s[-1] == '(':
        return False
    else:
        stack.append(s)
    for i in range(1,len(s)):
        a = s[i]
        if a != ')':
            stack.append(a)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
        
    return True
