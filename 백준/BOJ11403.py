import sys
import collections
read = sys.stdin.readline

n = int(read())
graph = collections.defaultdict(list)
stack = []
answer = []
for i in range(n):
    temp = []
    temp.extend(list(map(int, read().rstrip().split())))
    for j in range(n):
        if temp[j] == 1:
            graph[i].append(j)

for i in range(n):
    visit = [0 for j in range(n)]
    stack.append(i)
    while stack:
        node = stack.pop()
        for j in range(len(graph[node])):
            if visit[graph[node][j]] != 1:
                stack.append(graph[node][j])
                visit[graph[node][j]] = 1
    answer.append(visit)

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()
