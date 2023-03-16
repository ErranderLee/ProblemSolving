from collections import deque


def find_shortest_path(start, end, arr):
  len_x = len(arr)
  len_y = len(arr[0])
  dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  visit = set()
  q = deque()
  q.append((start, 0))
  visit.add(start)

  while q:
    cur, step = q.popleft()
    if cur == end:
      print(step)
      return step
    for dx, dy in dxdy:
      next_x = cur[0] + dx
      next_y = cur[1] + dy
      if (0 <= next_x < len_x and 0 <= next_y < len_y) and (next_x, next_y) not in visit and arr[next_x][next_y] != 'X':
        next_loc = (next_x, next_y)
        q.append((next_loc, step + 1))
        visit.add(next_loc)
  return -1


def solution(maps):
  answer = 0
  arr = []
  lever = (-1, -1)
  enter = (-1, -1)
  exit = (-1, -1)

  # 시작, 레버, 출구를 찾는다.
  for i, row in enumerate(maps):
    row_values = []
    for j, ch in enumerate(row):
      if ch == 'E':
        exit = (i, j)
      elif ch == 'L':
        lever = (i, j)
      elif ch == 'S':
        enter = (i, j)
      row_values.append(ch)
    arr.append(row_values)
  enter_lever = find_shortest_path(enter, lever, arr)
  if enter_lever == -1:
    return -1
  lever_exit = find_shortest_path(lever, exit, arr)
  if lever_exit == -1:
    return -1
  return enter_lever + lever_exit