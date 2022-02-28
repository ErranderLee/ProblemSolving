
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*m for i in range(n)]
    map = [[0]*m for i in range(n)]
    dp[0][0] = 1
    for puddle in puddles:
        map[puddle[1]-1][puddle[0]-1] = -1
    for i in range(1, m):
        if map[0][i] != -1:
            dp[0][i] = dp[0][i-1]
    for i in range(1, n):
        if map[i][0] != -1:
            dp[i][0] = dp[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            if map[i][j] != -1:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[n-1][m-1] % 1000000007
    return answer
print(solution(4,3,[[2,2]]))