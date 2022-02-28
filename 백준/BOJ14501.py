import sys
read = sys.stdin.readline

n = int(read())
table = []
dp = [0 for i in range(n)]
for i in range(n):
    table.append(list(map(int, read().rstrip().split())))

if table[-1][0] + n - 1 <= n:
    dp[-1] = table[-1][1]
else:
    dp[-1] = 0
for i in range(n-2, -1, -1):
    if i + table[i][0] <= n:
        if i + table[i][0] != n:
            dp[i] = max(dp[i + table[i][0]] + table[i][1], dp[i + 1])
        else:
            dp[i] = max(table[i][1], dp[i + 1])
    else:
        dp[i] = dp[i + 1]
print(dp[0])