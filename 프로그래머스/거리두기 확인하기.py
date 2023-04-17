
def check(place, i, j):
  dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  candidates = []
  stack = []
  stack.append((i, j, 0))
  visit = set()
  visit.add((i, j))
  while stack:
    x, y, dist = stack.pop()
    if dist == 2:
      continue
    for dx, dy in dxdy:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visit:
        stack.append((nx, ny, dist + 1))
        if place[nx][ny] == 'P':
          candidates.append((nx, ny))
  if len(candidates) == 0:
    return True

  for candidate in candidates:
    cx = candidate[0]
    cy = candidate[1]
    if abs(cx - i) + abs(cy - j) == 1:
      return False
    if cx != i and cy != j:
      if not (place[cx][j] == 'X' and place[i][cy] == 'X'):
        return False
    else:
      if place[(cx + i) // 2][(cy +j) // 2] != 'X':
        return False
  return True


def solution(places):
  answer = []
  for q, place in enumerate(places):
    flag = 1
    for i in range(len(place)):
      for j in range(len(place[0])):
        if place[i][j] == 'P':
          if not check(place, i, j):
            answer.append(0)
            flag = 0
            break
      if flag == 0:
        break
    if flag == 1:
      answer.append(1)
  return answer