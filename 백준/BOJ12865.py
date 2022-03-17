import sys; read=sys.stdin.readline

n, k = list(map(int, read().rstrip().split()))
dp = [[0 for i in range(k+1)] for j in range(n+1)]
weights = [0]
values = [0]
for i in range(n):
    temp = list(map(int, read().rstrip().split()))
    weights.append(temp[0])
    values.append(temp[1])

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= weights[i]:
            dp[i][j] = max(dp[i-1][j], values[i] + dp[i-1][j-weights[i]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])
