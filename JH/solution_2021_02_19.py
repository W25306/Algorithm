def solution(n,a,b):
    answer = 1
    if n == 2:
        return answer
    if a > b:
        while True:
            if a == b + 1 and b % 2 == 1 and a % 2 == 0 :
                break
            if a % 2 == 1:
                a = a//2 + 1
            else:
                a = a // 2
            if b % 2 == 1:
                b = b // 2 + 1
            else:
                b = b // 2
            if a == 1 and b == 1:
                break
            elif a == b+1 and b % 2 == 1 and a % 2 == 0:
                answer += 1
                break
            else:
                answer += 1
    else:
        while True:
            if a + 1 == b and b % 2 == 0 and a % 2 == 1:
                break
            if a % 2 == 1:
                a = a//2 + 1
            else:
                a = a // 2
            if b % 2 == 1:
                b = b // 2 + 1
            else:
                b = b // 2
            if a +1 == b and b % 2 == 0 and a % 2 == 1:
                answer += 1
                break
            else:
                answer += 1
    print(answer)


    return answer