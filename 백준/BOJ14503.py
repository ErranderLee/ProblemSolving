import sys

input = sys.stdin.readline
n, m = list(map(int, input().rstrip().split()))
r, c, d = list(map(int, input().rstrip().split()))
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pos = (r, c)
answer = 1
count = 0
cleaned = [[False for _ in range(m)] for _ in range(n)]
cleaned[r][c] = True

while True:
    d -= 1
    if d < 0:
        d = 4 + d
    temp = (pos[0] + dxdy[d][0], pos[1] + dxdy[d][1])
    if maps[temp[0]][temp[1]] == 0 and not cleaned[temp[0]][temp[1]]:
        cleaned[temp[0]][temp[1]] = True
        answer += 1
        count = 0
        pos = temp
        continue
    else:
        count += 1
        if count == 4:
            back_pos = (pos[0] - dxdy[d][0], pos[1] - dxdy[d][1])
            if maps[back_pos[0]][back_pos[1]] == 0:
                count = 0
                pos = back_pos
                continue
            else:
                print(answer)
                sys.exit(0)
        continue

