import sys
read = sys.stdin.readline

n, m = list(map(int, read().rstrip().split()))
arr = []
dp = [[0 for i in range(n)] for i in range(n)]
questions = []
answers = []
for i in range(n):
    arr.append(list(map(int, read().rstrip().split())))
for i in range(m):
    questions.append(list(map(int, read().rstrip().split())))


for i in range(n):
    for j in range(n):
        if j == 0:
            dp[i][j] += arr[i][j]
        else:
            dp[i][j] += dp[i][j-1] + arr[i][j]

for question in questions:
    temp = 0
    for i in range(question[0]-1, question[2]):
        temp += dp[i][question[3]-1]
        if question[1]-2 >= 0:
            temp -= dp[i][question[1]-2]
    answers.append(temp)

for answer in answers:
    print(answer)