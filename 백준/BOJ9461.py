t = int(input())
ns = []

for i in range(t):
    ns.append(int(input()))
dp = [0 for i in range(max(ns))]
for i in range(t):
    for j in range(5):
        if j < 3:
            dp[j] = 1
        else:
            dp[j] = 2

    for j in range(5, ns[i]):
        dp[j] = dp[j-1] + dp[j-5]
for i in range(t):
    print(dp[ns[i]-1])

