import math


def get_coords_by_direction(direction):
    if direction == 0: # 서쪽
        return [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (1, -1), (1, 0), (1, 1), (2, 0)]
    elif direction == 1: # 남쪽
        return [(0, -2), (1, -1), (0, -1), (-1, -1), (2, 0), (1, 1), (0, 1), (-1, 1), (0, 2)]
    elif direction == 2: # 동쪽
        return [(2, 0), (1, 1), (1, 0), (1, -1), (0, 2), (-1, 1), (-1, 0), (-1, -1), (-2, 0)]
    else: # 북쪽
        return [(0, 2), (-1, 1), (0, 1), (1, 1), (-2, 0), (-1, -1), (0, -1), (1, -1), (0, -2)]


if __name__ == '__main__':
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    proportion = [0.02,
                  0.10, 0.07, 0.01,
                  0.05,
                  0.10, 0.07, 0.01,
                  0.02]
    x = [n // 2, n // 2]
    y = [0, 0]
    direction = 0
    answer = 0
    move_amount = 0
    for i in range(n - 1):
        if i < n - 2:
            move_amount = 2
        else:
            move_amount = 3
        for j in range(move_amount):
            for k in range(i + 1):
                sum_of_fly_sand = 0
                y[0] = x[0] + dx[direction]
                y[1] = x[1] + dy[direction]
                coords = get_coords_by_direction(direction)
                for l, coord in enumerate(coords):
                    node_fly_sand = (y[0] + coord[0], y[1] + coord[1])
                    amount_fly_sand = math.floor(maps[y[0]][y[1]] * proportion[l])
                    sum_of_fly_sand += amount_fly_sand
                    if 0 <= node_fly_sand[0] < n and 0 <= node_fly_sand[1] < n:
                        maps[node_fly_sand[0]][node_fly_sand[1]] += amount_fly_sand
                    else:
                        answer += amount_fly_sand
                node_alpha = (y[0] + dx[direction], y[1] + dy[direction])
                maps[y[0]][y[1]] -= sum_of_fly_sand
                if 0 <= node_alpha[0] < n and 0 <= node_alpha[1] < n:
                    maps[node_alpha[0]][node_alpha[1]] += maps[y[0]][y[1]]
                else:
                    answer += maps[y[0]][y[1]]
                maps[y[0]][y[1]] = 0
                x[0] += dx[direction]
                x[1] += dy[direction]
            # 방향 전환
            direction = (direction + 1) % 4
    print(answer)



