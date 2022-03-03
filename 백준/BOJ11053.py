import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().rstrip().split()))
dp = [1 for i in range(n)]

dp[0] = 1
for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))