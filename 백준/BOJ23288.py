# 0 2 0
# 4 1 3
# 0 5 0
# 0 6 0

# 동쪽으로 이동
# 0 2 0
# 6 4 1
# 0 5 0
# 0 3 0

# 0 2 0
# 3 6 4
# 0 5 0
# 0 1 0

# 서쪽으로 이동
# 0 2 0
# 1 3 6
# 0 5 0
# 0 4 0

# 남쪽으로 이동
# 0 6 0
# 4 2 3
# 0 1 0
# 0 5 0

# 북쪽으로 이동
# 0 1 0
# 4 5 3
# 0 6 0
# 0 2 0
import copy


def roll_dice(dice, direction):
    # 동
    if direction == 0:
        dice[1][2], dice[1][1] = dice[1][1], dice[1][2]
        dice[1][1], dice[1][0] = dice[1][0], dice[1][1]
        dice[1][0], dice[3][1] = dice[3][1], dice[1][0]
    # 남
    elif direction == 1:
        dice[0][1], dice[3][1] = dice[3][1], dice[0][1]
        dice[3][1], dice[2][1] = dice[2][1], dice[3][1]
        dice[2][1], dice[1][1] = dice[1][1], dice[2][1]
    # 서
    elif direction == 2:
        dice[1][0], dice[1][1] = dice[1][1], dice[1][0]
        dice[1][1], dice[1][2] = dice[1][2], dice[1][1]
        dice[1][2], dice[3][1] = dice[3][1], dice[1][2]
    # 북
    elif direction == 3:
        dice[0][1], dice[3][1] = dice[3][1], dice[0][1]
        dice[0][1], dice[1][1] = dice[1][1], dice[0][1]
        dice[1][1], dice[2][1] = dice[2][1], dice[1][1]

    return dice


def calc_point(coord, maps):
    return dfs(coord, maps) * maps[coord[0]][coord[1]]


def dfs(coord, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    count = 1
    stack = []
    visit = set()
    stack.append(coord)
    visit.add(coord)
    while stack:
        popped_coord = stack.pop()
        for i in range(4):
            x = popped_coord[0] + dx[i]
            y = popped_coord[1] + dy[i]
            if 0 <= x < n and 0<= y < m and maps[x][y] == maps[coord[0]][coord[1]] and (x, y) not in visit:
                stack.append((x, y))
                count += 1
                visit.add((x, y))

    return count


def get_floor(dice):
    return dice[3][1]


def get_direction(floor, coord, maps, direction):
    pos_val = maps[coord[0]][coord[1]]
    if floor < pos_val:
        if direction - 1 < 0:
            return 3
        else:
            return direction - 1
    elif floor > pos_val:
        return (direction + 1) % 4
    else:
        return direction


def get_coord(old_coord, direction):
    if direction == 0:
        return old_coord[0], old_coord[1] + 1
    elif direction == 1:
        return old_coord[0] + 1, old_coord[1]
    elif direction == 2:
        return old_coord[0], old_coord[1] - 1
    elif direction == 3:
        return old_coord[0] - 1, old_coord[1]


def can_go(old_coord, direction, n, m):
    if direction == 0:
        return old_coord[1] + 1 < m
    elif direction == 1:
        return old_coord[0] + 1 < n
    elif direction == 2:
        return old_coord[1] - 1 >= 0
    elif direction == 3:
        return old_coord[0] - 1 >= 0


def move_dice(initial_dice, k, maps):
    direction = 0
    coord = (0, 0)
    n = len(maps)
    m = len(maps[0])
    sum = 0
    rolled_dice = copy.deepcopy(initial_dice)
    for _ in range(k):
        if not can_go(coord, direction, n, m):
            direction = (direction + 2) % 4

        rolled_dice = roll_dice(rolled_dice, direction)
        coord = get_coord(coord, direction)
        direction = get_direction(get_floor(rolled_dice), coord, maps, direction)
        sum += calc_point(coord, maps)

    return sum


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    initial_dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
    print(move_dice(initial_dice, k, maps))
