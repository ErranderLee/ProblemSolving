import sys

n = int(input())
cost = []
memo = [[0] * 3 for i in range(n)]
for i in range(n):
    cost.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(3):
    memo[0][i] = cost[0][i]
for i in range(1, n):
    memo[i][0] += cost[i][0] + min(memo[i-1][1], memo[i-1][2])
    memo[i][1] += cost[i][1] + min(memo[i-1][0], memo[i-1][2])
    memo[i][2] += cost[i][2] + min(memo[i-1][0], memo[i-1][1])
print(min(memo[-1]))

