from collections import deque


def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    h = len(maps)
    w = len(maps[0])
    answer = -1
    visit = [[0] * w for _ in range(h)]
    visit[0][0] = 1
    q = deque()
    q.append((0, 0, 1))
    visit[0][0] = 1
    while q:
        x, y, count = q.popleft()
        for i in range(4):
            f_x = x + dx[i]
            f_y = y + dy[i]
            if 0 <= f_x < h and 0 <= f_y < w:
                if f_x == h - 1 and f_y == w - 1:
                    return count + 1
                if visit[f_x][f_y] == 0 and maps[f_x][f_y] == 1:
                    visit[f_x][f_y] = 1
                    q.append((f_x, f_y, count + 1))

    return answer
