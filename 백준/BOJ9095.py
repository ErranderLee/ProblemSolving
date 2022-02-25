t = int(input())
answer = []
numbers = []
memo = [0] * 11

for i in range(t):
    numbers.append(int(input()))

memo[1] = 1
memo[2] = 2
memo[3] = 4

def solution(x):
    if x == 1:
        return memo[1]
    elif x == 2:
        return memo[2]
    elif x == 3:
        return memo[3]
    else:
        memo[x] = solution(x - 1) + solution(x - 2) + solution(x - 3)
        return memo[x]

for number in numbers:
    answer.append(solution(number))

for ans in answer:
    print(ans)

