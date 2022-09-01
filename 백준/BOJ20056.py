import collections


def get_direction(direction):
    dx, dy = 0, 0
    if direction == 0:
        dx -= 1
    elif direction == 1:
        dx -= 1
        dy += 1
    elif direction == 2:
        dy += 1
    elif direction == 3:
        dx += 1
        dy += 1
    elif direction == 4:
        dx += 1
    elif direction == 5:
        dx += 1
        dy -= 1
    elif direction == 6:
        dy -= 1
    else:
        dx -= 1
        dy -= 1

    return dx, dy


def move_fireball(count_dict, n):
    new_count_dict = collections.defaultdict(list)
    for key in count_dict.keys():
        for value in count_dict[key]:
            dx, dy = get_direction(value[1])
            new_x = (key[0] + dx * value[2]) % n
            new_y = (key[1] + dy * value[2]) % n
            new_count_dict[(new_x, new_y)].append([value[0], value[1], value[2]])
    return new_count_dict


def divide_fireball(count_dict):
    new_count_dict = collections.defaultdict(list)
    for key in count_dict.keys():
        if len(count_dict[key]) >= 2:
            divided_mass = 0
            divided_speed = 0
            divided_direction = [0, 2, 4, 6]
            res = count_dict[key][0][1] % 2
            for value in count_dict[key]:
                divided_mass += value[0]
                divided_speed += value[2]
                if value[1] % 2 != res:
                    divided_direction = [1, 3, 5, 7]
            divided_mass = divided_mass // 5
            divided_speed = divided_speed // len(count_dict[key])
            if divided_mass > 0:
                for i in range(4):
                    new_count_dict[key].append([divided_mass, divided_direction[i], divided_speed])
        elif len(count_dict[key]) == 1:
            new_count_dict[key].append(count_dict[key][0])
    return new_count_dict


if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    inputs = [list(map(int, input().split())) for _ in range(m)]
    coords = []
    masses = []
    directions = []
    speeds = []
    count_dict = collections.defaultdict(list)
    for input in inputs:
        coords.append([input[0] - 1, input[1] - 1])
        masses.append(input[2])
        speeds.append(input[3])
        directions.append(input[4])

    for i in range(len(coords)):
        count_dict[(coords[i][0], coords[i][1])].append([masses[i], directions[i], speeds[i]])

    for i in range(k):
        count_dict = divide_fireball(move_fireball(count_dict, n))

    answer = 0
    for values in count_dict.values():
        for value in values:
            answer += value[0]

    print(answer)