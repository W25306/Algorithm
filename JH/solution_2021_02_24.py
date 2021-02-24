def solution(s):
    answer = 0
    b = len(s)
    result = ''
    if len(s) == 1:
        return 1
    split_num = list(range(1,b//2+1))
    stack = []
    for i in range(1,b//2+1):
        count = 1
        temp = s[:i]
        for j in range(i,b,i):
            if s[j:j+i] == temp:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp
                temp = s[j:j+i]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + temp
        # print(result)
        stack.append(len(result))
        result = ""
    # print(stack)
    return min(stack)
