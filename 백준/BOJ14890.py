import sys


def check(arr):
    stack = 1
    floor = arr[0]
    pos = 1
    while True:
        if pos >= n:
            return 1
        if floor > arr[pos]:
            if floor - 1 != arr[pos]:
                return 0
            for j in range(pos, pos + l):
                if j >= n:
                    return 0
                if arr[j] != floor - 1:
                    return 0
            if pos + l == n:
                return 1
            if pos + l < n and arr[pos + l] <= arr[pos]:
                pos += l
                stack = 0
                floor -= 1
                continue
            else:
                return 0
        elif floor < arr[pos]:
            if floor + 1 != arr[pos]:
                return 0
            if stack >= l:
                floor = arr[pos]
                stack = 1
                pos += 1
            else:
                return 0
        else:
            pos += 1
            stack += 1


if __name__ == '__main__':
    input = sys.stdin.readline
    n, l = map(int, input().rstrip().split())
    maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        if check(maps[i]):
            count += 1
        if check([maps[j][i] for j in range(n)]):
            count += 1
    print(count)
