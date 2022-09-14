import sys
import collections


input = sys.stdin.readline


def filter_first_cond(maps, favorite_students, student_num):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    count_dict = collections.defaultdict(list)
    for i in range(n):
        for j in range(n):
            count = 0
            if maps[i][j] == 0:
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < n and maps[x][y] in favorite_students[student_num]:
                        count += 1
                count_dict[count].append((i, j))
    return count_dict[max(count_dict.keys())]


def filter_second_cond(maps, upper_result):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    count_dict = collections.defaultdict(list)
    for node in upper_result:
        count = 0
        for i in range(4):
            x = node[0] + dx[i]
            y = node[1] + dy[i]
            if 0 <= x < n and 0 <= y < n and maps[x][y] == 0:
                count += 1
        count_dict[count].append((node[0], node[1]))
    return count_dict[max(count_dict.keys())]


def filter_third_cond(upper_result):
    upper_result.sort(key=lambda x: (x[0], x[1]))
    return upper_result


def calc_score(maps, favorite_students):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    sum = 0
    n = len(maps)
    for i in range(n):
        for j in range(n):
            count = 0
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < n and maps[x][y] in favorite_students[maps[i][j]]:
                    count += 1
            if count == 1:
                sum += 1
            elif count == 2:
                sum += 10
            elif count == 3:
                sum += 100
            elif count == 4:
                sum += 1000
    return sum


if __name__ == '__main__':
    n = int(input().rstrip())
    maps = [[0 for _ in range(n)] for _ in range(n)]
    favorite_students = collections.defaultdict(list)
    for i in range(n*n):
        temp = list(map(int, input().rstrip().split()))
        favorite_students[temp[0]].extend(temp[1:])
    for student_num in favorite_students.keys():
        first_filter = filter_first_cond(maps, favorite_students, student_num)
        if len(first_filter) == 1:
            maps[first_filter[0][0]][first_filter[0][1]] = student_num
        else:
            second_filter = filter_second_cond(maps, first_filter)
            if len(second_filter) == 1:
                maps[second_filter[0][0]][second_filter[0][1]] = student_num
            else:
                third_filter = filter_third_cond(second_filter)
                maps[third_filter[0][0]][third_filter[0][1]] = student_num
    print(calc_score(maps, favorite_students))
