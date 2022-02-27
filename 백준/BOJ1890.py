import sys
read = sys.stdin.readline

n = int(read())
board = []
dp = [[0] * n for i in range(n)]
for i in range(n):
    board.append(list(map(int, read().rstrip().split())))
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[board[0][0]][0] = 1
            dp[0][board[0][0]] = 1
        else:
            if dp[i][j] != 0:
                if i == n - 1 and j == n - 1:
                    break
                if i + board[i][j] < n:
                    dp[i+board[i][j]][j] += dp[i][j]
                if j + board[i][j] < n:
                    dp[i][j+board[i][j]] += dp[i][j]
print(dp[-1][-1])