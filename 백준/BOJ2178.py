import sys
import collections

n, m = list(map(int, input().split()))
miro = []
visit = [[0] * m for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = collections.deque()

for i in range(n):
    miro.append(list(sys.stdin.readline().rstrip()))

q.append([0, 0])
visit[0][0] = 1
while q:
    node = q.popleft()
    for i in range(4):
        x = node[0] + dx[i]
        y = node[1] + dy[i]
        if 0 <= x < n and 0<= y < m and miro[x][y] == '1' and visit[x][y] == 0:
            q.append([x, y])
            visit[x][y] = visit[node[0]][node[1]] + 1
print(visit[n-1][m-1])
