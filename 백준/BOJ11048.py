n, m = list(map(int, input().split()))
miro = []
dp = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    miro.append(list(map(int, input().split())))

dx = [-1, 0, -1]
dy = [-1, -1, 0]
for i in range(n):
    for j in range(m):
        for k in range(3):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < m:
                dp[i][j] = max(dp[i][j], dp[x][y])
        dp[i][j] += miro[i][j]
print(dp[n-1][m-1])