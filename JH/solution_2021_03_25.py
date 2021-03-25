def solution(n, money):
    answer = 0
    dp = [[0 for _ in range(n+1)] for _ in range(len(money))]
    dp[0][0] = 1

    for i in range(money[0], n+1,money[0]):
        dp[0][i] = 1
    for a in range(1,len(money)):
        for b in range(n+1):
            if b >= money[a]:
                dp[a][b] = (dp[a-1][b] + dp[a][b - money[a]])
            else:
                dp[a][b] = dp[a-1][b]

    return dp[-1][-1]
