import sys; read = sys.stdin.readline
import collections

n, m = list(map(int, read().rstrip().split()))
arr = []
for i in range(n):
    arr.append(list(map(int, read().rstrip())))
visit = [[[0, 0] for i in range(m)] for j in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = collections.deque()
    q.append((0, 0, 0))
    visit[0][0][0] = 1
    while q:
        pos_x, pos_y, isCrash = q.popleft()
        if pos_x == n - 1 and pos_y == m - 1:
            return visit[pos_x][pos_y][isCrash]
            sys.exit(0)
        for i in range(4):
            x = pos_x + dx[i]
            y = pos_y + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if arr[x][y] == 1 and isCrash == 0:
                    q.append((x, y, 1))
                    visit[x][y][1] = visit[pos_x][pos_y][isCrash] + 1
                elif arr[x][y] == 0 and visit[x][y][isCrash] == 0:
                    q.append((x, y, isCrash))
                    visit[x][y][isCrash] = visit[pos_x][pos_y][isCrash] + 1
    return -1
print(bfs())