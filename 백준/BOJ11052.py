import sys
read = sys.stdin.readline

n = int(read())
cards = list(map(int, read().rstrip().split()))
dp = [0] * n
dp[0] = cards[0]

for i in range(1, n):
    dp[i] = cards[i]
    for j in range(0, i):
        dp[i] = max(dp[i], dp[j] + cards[i-j-1])
print(dp[n-1])