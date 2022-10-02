from collections import deque
from itertools import permutations
import copy


def rotate(arr, query):
    q = deque()
    x1, y1, x2, y2 = query[0] - query[2] - 1, \
                     query[1] - query[2] - 1, \
                     query[0] + query[2] - 1, \
                     query[1] + query[2] - 1
    while (x1, y1) != (x2, y2):
        for i in range(y1, y2 + 1):
            q.append(arr[x1][i])
        for i in range(x1 + 1, x2 + 1):
            q.append(arr[i][y2])
        for i in range(y2 - 1, y1 - 1, -1):
            q.append(arr[x2][i])
        for i in range(x2 - 1, x1, -1):
            q.append(arr[i][y1])

        for i in range(y1 + 1, y2 + 1):
            arr[x1][i] = q.popleft()
        for i in range(x1 + 1, x2 + 1):
            arr[i][y2] = q.popleft()
        for i in range(y2 - 1, y1 - 1, -1):
            arr[x2][i] = q.popleft()
        for i in range(x2 - 1, x1 - 1, -1):
            arr[i][y1] = q.popleft()

        x1 += 1
        y1 += 1
        x2 -= 1
        y2 -= 1


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    queries = [list(map(int, input().split())) for _ in range(k)]
    answer = 250001
    min_value = 250001

    query_perms = list(permutations(queries, k))
    for candidates in query_perms:
        temp = copy.deepcopy(arr)
        for candidate in candidates:
            rotate(temp, candidate)
        for row in temp:
            min_value = min(min_value, sum(row))
        answer = min(answer, min_value)
    print(answer)
