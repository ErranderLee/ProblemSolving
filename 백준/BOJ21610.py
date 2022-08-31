

def create_cloud(n):
    # 차례로 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
    return [n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]


def move_cloud(cloud_coords, direction, distance):
    if direction == 1:
        dx, dy = 0, -1
    elif direction == 2:
        dx, dy = -1, -1
    elif direction == 3:
        dx, dy = -1, 0
    elif direction == 4:
        dx, dy = -1, 1
    elif direction == 5:
        dx, dy = 0, 1
    elif direction == 6:
        dx, dy = 1, 1
    elif direction == 7:
        dx, dy = 1, 0
    else:
        dx, dy = 1, -1

    for cloud_coord in cloud_coords:
        if distance >= n:
            distance = distance % n
        cloud_coord[0] += distance * dx
        cloud_coord[1] += distance * dy
    return cloud_coords


def convert_coords(cloud_coords, n):
    result = []
    for cloud_coord in cloud_coords:
        for i, coord in enumerate(cloud_coord):
            if coord < 0:
                cloud_coord[i] = n + coord
            else:
                cloud_coord[i] = coord % n
        result.append(cloud_coord)
    return result


def rain(cloud_coords, grid):
    for cloud_coord in cloud_coords:
        grid[cloud_coord[0]][cloud_coord[1]] += 1
    return grid


def copy_water(cloud_coords, grid):
    dx = [-1, 1, -1, 1]
    dy = [-1, 1, 1, -1]
    n = len(grid)
    for cloud_coord in cloud_coords:
        for i in range(4):
            x = cloud_coord[0] + dx[i]
            y = cloud_coord[1] + dy[i]
            if 0 <= x < n and 0 <= y < n and grid[x][y] > 0:
                grid[cloud_coord[0]][cloud_coord[1]] += 1
    return grid


def extract_water_and_create_new_cloud(cloud_coords, grid):
    n = len(grid)
    visit = [[0] * n for i in range(n)]
    for cloud_coord in cloud_coords:
        visit[cloud_coord[0]][cloud_coord[1]] = 1
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and visit[i][j] == 0:
                grid[i][j] -= 2
                new_cloud.append([i, j])
    return grid, new_cloud


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    direction_and_distance = [list(map(int, input().split())) for _ in range(m)]
    sum = 0
    clouds = create_cloud(n)
    for i in range(m):
        cloud_coords = convert_coords(
            move_cloud(
                clouds, direction_and_distance[i][0], direction_and_distance[i][1]
            ), n
        )
        grid, clouds = extract_water_and_create_new_cloud(cloud_coords, copy_water(cloud_coords, rain(cloud_coords, grid)))
    for i in range(n):
        for j in range(n):
            sum += grid[i][j]

    print(sum)