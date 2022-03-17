import itertools
import sys; read = sys.stdin.readline
import copy
import collections

n, m = list(map(int, read().rstrip().split()))
resMap = []
for i in range(n):
    resMap.append(read().rstrip().split())
canBuildWall = []
viruses = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(n):
    for j in range(m):
        if resMap[i][j] == '0':
            canBuildWall.append([i, j])
        elif resMap[i][j] == '2':
            viruses.append([i, j])

selectedWall = list(itertools.combinations(canBuildWall, 3))
maxValue = -1
for i in range(len(selectedWall)):
    temp = copy.deepcopy(resMap)
    q = collections.deque()
    visit = [[0 for k in range(m)] for l in range(n)]
    for j in range(3):
        temp[selectedWall[i][j][0]][selectedWall[i][j][1]] = '1'
    for virus in viruses:
        q.append(virus)
    while q:
        node = q.popleft()
        for j in range(4):
            x = node[0] + dx[j]
            y = node[1] + dy[j]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and temp[x][y] == '0':
                q.append([x, y])
                visit[x][y] = 1
                temp[x][y] = '2'
    count = 0
    for j in range(n):
        for k in range(m):
            if temp[j][k] == '0':
                count += 1
    maxValue = max(maxValue, count)
print(maxValue)





