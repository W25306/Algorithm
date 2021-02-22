def solution(n, words):
    answer = []
    stack = [words[0]]
    b = 0
    c = 0
    for i in range(1,len(words)):
        if words[i-1][-1] == words[i][0] and words[i] not in stack:
            stack.append(words[i])
        else:
            print(i)
            a = i + 1
            b = a % n

            if b == 0:
                b = n
            d = b
            while d != a:
                d += n
                c += 1
            c += 1
            break
    if stack == words:
        return [0,0]
    else:
        return [b,c]

    return answer