

dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def divide_group(picture, n):
    group_dict = dict()
    visit = [[False for _ in range(n)] for _ in range(n)]
    group_id = 0
    for i in range(n):
        for j in range(n):
            stack = []
            group = []
            if not visit[i][j]:
                group_dict[group_id] = [picture[i][j]]
                stack.append((i, j))
                visit[i][j] = True
                group.append((i, j))
                while stack:
                    node = stack.pop()
                    for k in range(4):
                        x = node[0] + dxdy[k][0]
                        y = node[1] + dxdy[k][1]
                        if 0 <= x < n and 0 <= y < n and not visit[x][y] and picture[x][y] == picture[i][j]:
                            visit[x][y] = True
                            group.append((x, y))
                            stack.append((x, y))
                group_dict[group_id].append(set(group))
                group_id += 1
    return group_dict


def calc_score(group_dict, picture):
    result = 0
    keys = group_dict.keys()
    keys_len = len(keys)
    for i in range(keys_len):
        for j in range(i + 1, keys_len):
            count = 0
            comp_values1 = group_dict[i][1]
            comp_values2 = group_dict[j][1]
            for x, y in comp_values1:
                for k in range(4):
                    adjx = x + dxdy[k][0]
                    adjy = y + dxdy[k][1]
                    if (adjx, adjy) in comp_values2:
                        count += 1
            result += (len(comp_values1) + len(comp_values2)) * group_dict[i][0] * group_dict[j][0] * count
    return result


def rotate(picture, n):
    mid = n // 2
    stack = []
    for i in range(n):
        stack.append(picture[mid][i])
        picture[mid][i] = picture[i][mid]
    for i in range(n):
        picture[i][mid] = stack.pop()
    for k in range(4):
        if k == 0:
            x, y = (0, 0)
        elif k == 1:
            x, y = (0, n // 2 + 1)
        elif k == 2:
            x, y = (n // 2 + 1, 0)
        else:
            x, y = (n // 2 + 1, n // 2 + 1)
        for i in range(n // 2):
            for j in range(i, n // 2):
                if i != j:
                    picture[x + i][y + j], picture[x + j][y + i] = picture[x + j][y + i], picture[x + i][y + j]
        for i in range(n // 2):
            picture[x + i][y:y + n//2] = reversed(picture[x + i][y:y + n // 2])


if __name__ == '__main__':
    n = int(input())
    picture = [list(map(int, input().rstrip().split())) for _ in range(n)]
    answer = 0
    answer += calc_score(divide_group(picture, n), picture)
    for i in range(3):
        rotate(picture, n)
        answer += calc_score(divide_group(picture, n), picture)
    print(answer)