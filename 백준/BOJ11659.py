import sys
read = sys.stdin.readline

n, m = list(map(int, read().rstrip().split()))
arr = []
questions = []
arr.extend(list(map(int, read().rstrip().split())))
dp = [0 for i in range(n)]
for i in range(m):
    questions.append(list(map(int, read().rstrip().split())))

dp[0] = arr[0]
for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]
for question in questions:
    if question[0] - 1 == 0:
        print(dp[question[1]-1])
    else:
        print(dp[question[1]-1] - dp[question[0]-2])