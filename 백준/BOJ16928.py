import sys; read=sys.stdin.readline
from collections import deque

n, m = list(map(int, read().rstrip().split()))
ladders = dict()
snakes = dict()
visit = [0 for i in range(101)]

for i in range(n):
    temp = list(map(int, read().rstrip().split()))
    ladders[temp[0]] = temp[1]
for i in range(m):
    temp = list(map(int, read().rstrip().split()))
    snakes[temp[0]] = temp[1]

answer = 0
q = deque()
q.append(1)

while q:
    node = q.popleft()
    if node == 100:
        answer = visit[100]
        break
    for i in range(1, 7):
        nextNode = node + i
        if nextNode in ladders.keys():
            nextNode = ladders[nextNode]
        if nextNode in snakes.keys():
            nextNode = snakes[nextNode]
        if nextNode <= 100 and visit[nextNode] == 0:
            q.append(nextNode)
            visit[nextNode] = visit[node] + 1
print(answer)