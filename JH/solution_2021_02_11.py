def solution(n):
    answer = 0
#     a = []
#     i = 1
#     while i <= n//2 + 1:
#         a = i
#         for j in range(i+1,n//2+2):
#             a += j
#             if a == n:
#                 answer += 1
#         i += 1
    for i in range(1,n+1,2):
        mod = n % i
        if mod == 0:
            answer += 1
    return answer
    
    # i - 1 i i + 1 => 3i
    # 즉 3의 배수다. 이것을 활용하여 3으로 떨어지는 약수 중의 홀수의 개수를 구하면 됨
