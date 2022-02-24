import sys
import collections

m, n = list(map(int, input().split()))
toms = []
q = collections.deque()
answer = 0
for i in range(n):
    toms.append(input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rippenToms = []
allRippen = 1
for i in range(n):
    for j in range(m):
        if toms[i][j] == '0':
            allRippen = 0
        elif toms[i][j] == '1':
            rippenToms.append([i, j])
if allRippen:
    print(0)
else:
    for tom in rippenToms:
        q.append([tom, 0])
    while q:
        temp = q.popleft()
        node = temp[0]
        count = temp[1]
        for i in range(4):
            x = node[0] + dx[i]
            y = node[1] + dy[i]
            if 0 <= x < n and 0 <= y < m and toms[x][y] == '0':
                q.append([[x, y], count + 1])
                toms[x][y] = '1'
    flag = 0
    for i in range(n):
        for j in range(m):
            if toms[i][j] == '0':
                print(-1)
                flag = 1
                break
        if flag:
            break
    if not flag:
        print(count)

