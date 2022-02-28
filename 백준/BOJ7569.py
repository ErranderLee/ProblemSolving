import sys
import collections
import copy
read = sys.stdin.readline

m, n, h = list(map(int, read().rstrip().split()))
boxes = []
q = collections.deque()
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
start = []
answer = 0
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, read().rstrip().split())))
    boxes.append(temp)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                start.append([i, j, k])
for i in range(len(start)):
    q.append([start[i], 0])
visit = copy.deepcopy(boxes)
while q:
    node = q.popleft()
    for i in range(6):
        x = node[0][0] + dx[i]
        y = node[0][1] + dy[i]
        z = node[0][2] + dz[i]
        if 0 <= x < h and 0 <= y < n and 0 <= z < m and visit[x][y][z] != 1 and boxes[x][y][z] == 0:
            q.append([[x, y, z], node[1] + 1])
            visit[x][y][z] = 1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if visit[i][j][k] == 0:
                print(-1)
                exit(0)
answer = node[1]
print(answer)








