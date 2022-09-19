import sys


def spread(maps, r, c):
    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maps[i][j] == 0:
                continue
            if maps[i][j] == -1:
                result[i][j] = -1
            else:
                result[i][j] += maps[i][j]
                spread_amount = maps[i][j] // 5
                if spread_amount == 0:
                    continue
                for k in range(4):
                    temp = (i + dxdy[k][0], j + dxdy[k][1])
                    if 0 <= temp[0] < r and 0 <= temp[1] < c and maps[temp[0]][temp[1]] != -1:
                        result[temp[0]][temp[1]] += spread_amount
                        result[i][j] -= spread_amount
    return result


def find_machine(maps, r):
    count = 0
    result = []
    for i in range(r):
        if maps[i][0] == -1:
            count += 1
            result.append((i, 0))
            if count == 2:
                return result


def wind(maps, r, c, machine_locs):
    result = [[0 for _ in range(c)] for _ in range(r)]
    for machine_loc in machine_locs:
        result[machine_loc[0]][machine_loc[1]] = -1
    # 위쪽
    for i in range(1, c - 1):
        result[machine_locs[0][0]][i + 1] += maps[machine_locs[0][0]][i]
        result[machine_locs[1][0]][i + 1] += maps[machine_locs[1][0]][i]
    for i in range(1, machine_locs[0][0] + 1):
        result[i - 1][c - 1] += maps[i][c - 1]
    for i in range(1, c):
        result[0][i - 1] += maps[0][i]
        result[r - 1][i - 1] += maps[r - 1][i]
    for i in range(0, machine_locs[0][0] - 1):
        result[i + 1][0] += maps[i][0]

    for i in range(machine_locs[1][0], r - 1):
        result[i + 1][c - 1] += maps[i][c - 1]
    for i in range(machine_locs[1][0] + 2, r):
        result[i - 1][0] += maps[i][0]

    # 나머지 값 저장
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if i == machine_locs[0][0]:
                break
            if i == machine_locs[1][0]:
                break
            result[i][j] = maps[i][j]

    return result


if __name__ == '__main__':
    input = sys.stdin.readline
    r, c, t = map(int, input().rstrip().split())
    maps = [list(map(int, input().rstrip().split())) for _ in range(r)]
    machine_locs = find_machine(maps, r)
    for i in range(t):
        maps = wind(spread(maps, r, c), r, c, machine_locs)
    answer = 0
    for i in range(r):
        for j in range(c):
            if maps[i][j] == -1:
                continue
            answer += maps[i][j]
    print(answer)

