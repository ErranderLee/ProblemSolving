import sys
import collections
read = sys.stdin.readline

n = int(read())
painting = []
q = collections.deque()
visit = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    painting.append(list(read()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = [0, 0]

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            q.append([i, j])
            visit[i][j] = 1
            count[0] += 1
            while q:
                node = q.popleft()
                for k in range(4):
                    x = node[0] + dx[k]
                    y = node[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and painting[node[0]][node[1]] == painting[x][y] and visit[x][y] == 0:
                        q.append([x, y])
                        visit[x][y] = 1
for i in range(n):
    for j in range(n):
        if painting[i][j] == 'R':
            painting[i][j] = 'G'
visit = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            q.append([i, j])
            visit[i][j] = 1
            count[1] += 1
            while q:
                node = q.popleft()
                for k in range(4):
                    x = node[0] + dx[k]
                    y = node[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and painting[node[0]][node[1]] == painting[x][y] and visit[x][y] == 0:
                        q.append([x, y])
                        visit[x][y] = 1
print(count[0], count[1])
