import sys

n = int(input())
steps = []
memo = [0] * n
for i in range(n):
    steps.append(int(sys.stdin.readline().rstrip()))
if n == 1:
    print(steps[0])
elif n == 2:
    print(steps[0] + steps[1])
else:
    memo[0] = steps[0]
    memo[1] = steps[0] + steps[1]
    memo[2] = steps[2] + max(steps[1], memo[0])

    for i in range(3, n):
        memo[i] = steps[i] + max(memo[i-3] + steps[i-1], memo[i-2])
    print(memo[-1])