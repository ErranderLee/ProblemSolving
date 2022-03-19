import sys; read = sys.stdin.readline

s1 = read().rstrip()
s2 = read().rstrip()
dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
print(dp[len(s2)][len(s1)])

