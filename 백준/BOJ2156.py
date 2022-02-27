import sys

n = int(input())
wines = []
for i in range(n):
    wines.append(int(sys.stdin.readline().rstrip()))
if n == 1:
    print(wines[0])
elif n == 2:
    print(wines[0] + wines[1])
elif n == 3:
    print(max(wines[0] + wines[1], wines[2] + max(wines[1], wines[0])))
else:
    dp = [0] * n
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(dp[1], wines[2] + max(wines[1], wines[0]))
    for i in range(3, n):
        dp[i] = max(wines[i] + dp[i-3] + wines[i-1], wines[i] + dp[i-2], dp[i-1])
    print(dp[-1])