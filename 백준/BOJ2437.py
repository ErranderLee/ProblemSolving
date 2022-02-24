import sys

n = int(input())
weights = list(map(int, sys.stdin.readline().split()))
sum = 0
answer = 0

weights.sort()
for weight in weights:
    if sum + 1 >= weight:
        sum += weight
    answer = sum + 1
print(answer)