import math
import sys

input = sys.stdin.readline


def rotate(A, l):
    length = len(A[0])
    result = [[0 for _ in range(length)] for _ in range(length)]
    hop = int(math.pow(2, l))
    for i in range(0, length, hop):
        for j in range(0, length, hop):
            for k in range(i, i + hop):
                for l in range(j, j + hop):
                    result[i + l - j][j + hop - 1 - (k-i)] = A[k][l]

    return result


def melt(A):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    length = len(A[0])
    result = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            count = 0
            result[i][j] = A[i][j]
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < length and 0 <= y < length and A[x][y] > 0:
                    count += 1
                if count >= 3:
                    result[x][y] = A[x][y]
                    break
            if count < 3:
                if A[i][j] > 1:
                    result[i][j] = A[i][j] - 1
                elif A[i][j] == 1:
                    result[i][j] = 0
    return result


def dfs(A):
    max_ice = 0
    length = len(A[0])

    visit = [[0 for _ in range(length)] for _ in range(length)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(length):
        for j in range(length):
            stack = []
            if visit[i][j] == 0:
                stack.append((i, j))
                visit[i][j] = 1
                count = 0
                if A[i][j] > 0:
                    count += 1
                while stack:
                    node = stack.pop()
                    for k in range(4):
                        x = node[0] + dx[k]
                        y = node[1] + dy[k]
                        if 0 <= x < length and 0 <= y < length and visit[x][y] == 0 and A[x][y] > 0:
                            stack.append((x, y))
                            visit[x][y] = 1
                            count += 1
                max_ice = max(max_ice, count)
    return max_ice


if __name__ == '__main__':
    n, q = list(map(int, input().rstrip().split()))
    A = [list(map(int, input().rstrip().split())) for _ in range(int(math.pow(2, n)))]
    ls = list(map(int, input().rstrip().split()))

    for l in ls:
        A = rotate(A, l)
        A = melt(A)

    total = 0
    length = len(A[0])

    for line in A:
        total += sum(line)

    print(total)
    print(dfs(A))