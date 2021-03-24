def solution(n):
    answer = 0
    
    bef1 = 1
    bef2 = 2
    
    for i in range(2,n):
        answer = bef1 + bef2
        bef1 = bef2
        bef2 = answer
    
    return answer % 1000000007
