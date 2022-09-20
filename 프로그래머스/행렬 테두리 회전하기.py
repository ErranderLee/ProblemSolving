import collections


def rotate(maps, query):
    x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
    q = collections.deque()
    for i in range(y1, y2 + 1):
        q.append(maps[x1][i])
    for i in range(x1 + 1, x2 + 1):
        q.append(maps[i][y2])
    for i in range(y2 - 1, y1 - 1, -1):
        q.append(maps[x2][i])
    for i in range(x2 - 1, x1, -1):
        q.append(maps[i][y1])
    min_value = min(q)
    for i in range(y1 + 1, y2 + 1):
        maps[x1][i] = q.popleft()
    for i in range(x1 + 1, x2 + 1):
        maps[i][y2] = q.popleft()
    for i in range(y2 - 1, y1 - 1, -1):
        maps[x2][i] = q.popleft()
    for i in range(x2 - 1, x1 - 1, -1):
        maps[i][y1] = q.popleft()

    return min_value


def solution(rows, columns, queries):
    answer = []
    maps = [[0 for i in range(columns)] for j in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            maps[i][j] = count
            count += 1
    for query in queries:
        answer.append(rotate(maps, query))

    return answer