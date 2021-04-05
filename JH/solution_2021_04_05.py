def solution(A, B):
    answer = 0
    A = sorted(A,reverse=True)
    B = sorted(B)
    s = -1

    for i in range(len(A)):
        a = B[s]
        if A[i] >= a:
            continue
        else:
            s -= 1
            answer += 1
    return answer
