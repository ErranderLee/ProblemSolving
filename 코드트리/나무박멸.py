

dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def grow(maps, n):
    trees = set()
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 0:
                trees.add((i, j))
                count = 0
                for k in range(4):
                    x = i + dxdy[k][0]
                    y = j + dxdy[k][1]
                    if 0 <= x < n and 0 <= y < n and maps[x][y] > 0:
                        count += 1
                maps[i][j] += count
    return trees


def reproduce(trees, maps, n, polluted_nodes, now, c):
    place_trees_spawn = set()
    for i, j in trees:
        exist = []
        for k in range(4):
            x = i + dxdy[k][0]
            y = j + dxdy[k][1]
            if 0 <= x < n and 0 <= y < n and (x, y) not in trees:
                check = True
                if (x, y) in polluted_nodes:
                    if polluted_nodes[(x, y)] + c >= now:
                        check = False
                if maps[x][y] >= 0 and check:
                    exist.append(k)
        if exist:
            num_tree_to_reproduce = maps[i][j] // len(exist)
            for k in exist:
                maps[i + dxdy[k][0]][j + dxdy[k][1]] += num_tree_to_reproduce
                place_trees_spawn.add((i + dxdy[k][0], j + dxdy[k][1]))
    return trees.union(place_trees_spawn)


def find_proper_place(maps, n, trees, polluted_nodes, k, now):
    trees = sorted(trees)
    # 4개의 대각선 방향
    diags = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    max_count = 0
    new_polluted_nodes = dict()
    for i, j in trees:
        count = 0
        count += maps[i][j]
        can_go = [0, 1, 2, 3]
        polluted = dict()
        polluted[(i, j)] = now
        temp_store_cannot_go = []
        for dist in range(1, k + 1):
            for diag in temp_store_cannot_go:
                if diag in can_go:
                    can_go.remove(diag)
            for diag in can_go:
                x = i + diags[diag][0] * dist
                y = j + diags[diag][1] * dist
                if 0 <= x < n and 0 <= y < n:
                    polluted[(x, y)] = now
                    if maps[x][y] > 0:
                        count += maps[x][y]
                    elif maps[x][y] == -1 or maps[x][y] == 0:
                        temp_store_cannot_go.append(diag)
        if max_count < count:
            new_polluted_nodes = polluted
            max_count = count
    for i, j in new_polluted_nodes:
        polluted_nodes[(i, j)] = new_polluted_nodes[(i, j)]
    return max_count


def pollute(maps, polluted_nodes, now):

    for i, j in polluted_nodes:
        if maps[i][j] != -1 and polluted_nodes[(i, j)] ==  now:
            maps[i][j] = 0


if __name__ == '__main__':
    n, m, k, c = map(int, input().rstrip().split())
    maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
    polluted_nodes = dict()
    answer = 0
    for i in range(m):
        trees = grow(maps, n)
        trees = reproduce(trees, maps, n, polluted_nodes, i, c)
        answer += find_proper_place(maps, n, trees, polluted_nodes, k, i)
        pollute(maps, polluted_nodes, i)

    print(answer)
