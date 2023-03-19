
def check_valid_loc(new_x, new_y, height, width, visit, maps):
  if not (0 <= new_x < height and 0 <= new_y < width):
    return False
  if (new_x, new_y) in visit:
    return False
  if (maps[new_x][new_y] == 'X'):
    return False

  return True


def solution(maps):
  answer = []
  height = len(maps)
  width = len(maps[0])
  stack = []
  dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  visit = set()

  for i in range(height):
    for j in range(width):
      if maps[i][j] != 'X' and (i, j) not in visit:
        total = 0
        stack.append((i, j))
        visit.add((i, j))
        total += int(maps[i][j])
        while stack:
          x, y = stack.pop()
          for dx, dy in dxdy:
            new_x = x + dx
            new_y = y + dy
            if check_valid_loc(new_x, new_y, height, width, visit, maps):
              total += int(maps[new_x][new_y])
              stack.append((new_x, new_y))
              visit.add((new_x, new_y))
        answer.append(total)
  if len(answer) == 0:
    return [-1]
  return sorted(answer)