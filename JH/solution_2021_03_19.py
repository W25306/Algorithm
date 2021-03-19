def solution(s):
    answer = []
    s = s[1:-1]
    s = s.split('}')
    arr = []
    for i in range(len(s)):
        temp = s[i]
        t_arr = []
        temp = temp.split(',')
        if i != 0:
            temp.pop(0)
        for j in range(len(temp)):
            if j == 0:
                a = temp[j]
                a = a.replace('{','')
                temp[j] = a
            if temp[j].isdigit():
                t_arr.append(int(temp[j]))
        arr.append([len(t_arr),t_arr])
    arr = arr[:-1]
    if len(arr) == 1:
        return arr[0][1]
    else:
        stack = []
        s = sorted(arr)
        for i in range(len(s[0][1])):
            stack.append(s[0][1][i])
        for i in range(1,len(s)):
            t = s[i][1]
            for j in range(len(t)):
                if t[j] in stack:
                    continue
                else:
                    stack.append(t[j])
        
    return stack
