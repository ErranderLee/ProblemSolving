import sys; read=sys.stdin.readline
import copy

n = int(read())
arr = list(map(int, read().rstrip().split()))
dp = copy.deepcopy(arr)

for i in range(0, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))

