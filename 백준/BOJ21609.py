import sys
import collections


def find_largest_block_group(maps, block_groups):
    largest_block_group = []
    for block_group in block_groups:
        if len(largest_block_group) < len(block_group):
            largest_block_group = []
            largest_block_group.extend(block_group)
        elif len(largest_block_group) == len(block_group):
            largest_block_group_rainbow_count = 0
            block_group_rainbow_count = 0
            for i in range(len(largest_block_group)):
                if maps[block_group[i][0]][block_group[i][1]] == 0:
                    block_group_rainbow_count += 1
                if maps[largest_block_group[i][0]][largest_block_group[i][1]] == 0:
                    largest_block_group_rainbow_count += 1
            if block_group_rainbow_count > largest_block_group_rainbow_count:
                largest_block_group = []
                largest_block_group.extend(block_group)
            elif block_group_rainbow_count == largest_block_group_rainbow_count:
                temp = []
                temp.append((block_group[0][0], block_group[0][1], 0))
                temp.append((largest_block_group[0][0], largest_block_group[0][1], 1))
                temp.sort(key=lambda x: (x[0], x[1]), reverse=True)
                if temp[0][2] == 0:
                    largest_block_group = []
                    largest_block_group.extend(block_group)
    return largest_block_group


def find_block_groups(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    visit = [[False for _ in range(n)] for _ in range(n)]
    block_groups = []
    q = collections.deque()
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False and maps[i][j] != -1 and maps[i][j] != 0 and maps[i][j] != -2:
                blocks = []
                q.append((i, j))
                blocks.append((i, j))
                visit[i][j] = True
                rainbows = []
                while q:
                    node = q.popleft()
                    for k in range(4):
                        x = node[0] + dx[k]
                        y = node[1] + dy[k]
                        if 0 <= x < n and 0 <= y < n and visit[x][y] == False:
                            if maps[x][y] != -2 and maps[x][y] != -1:
                                if maps[x][y] == 0 or maps[i][j] == maps[x][y]:
                                    blocks.append((x, y))
                                    q.append((x, y))
                                    visit[x][y] = True
                                    if maps[x][y] == 0:
                                        rainbows.append((x, y))
                for rainbow in rainbows:
                    visit[rainbow[0]][rainbow[1]] = False
                if len(blocks) > 1:
                    block_groups.append(blocks)
    return block_groups


def remove_blocks(maps, largest_block_group):
    for block in largest_block_group:
        maps[block[0]][block[1]] = -2


def apply_gravity(maps):
    n = len(maps)
    for i in range(n-2, -1, -1):
        for j in range(n):
            if maps[i][j] != -1:
                pos = i
                while True:
                    if pos + 1 < n and maps[pos+1][j] == -2:
                        maps[pos][j], maps[pos+1][j] = maps[pos+1][j], maps[pos][j]
                        pos = pos + 1
                    else:
                        break


def rotate(maps):
    maps = list(zip(*maps))[::-1]
    result = []
    for map in maps:
        result.append(list(map))
    return result


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = list(map(int, input().rstrip().split()))
    maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
    sum = 0

    while True:
        groups = find_block_groups(maps)
        if len(groups) == 0:
            break
        largest_block_group = find_largest_block_group(maps, groups)
        sum += len(largest_block_group) * len(largest_block_group)
        remove_blocks(maps, largest_block_group)
        apply_gravity(maps)
        maps = rotate(maps)
        apply_gravity(maps)

    print(sum)




