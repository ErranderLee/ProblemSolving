from collections import deque


def find_end(board, start, dxdy):
  dx, dy = dxdy
  index = 0
  width = len(board)
  height = len(board[0])
  while True:
    index += 1
    new_x, new_y = start[0] + dx * index, start[1] + dy * index
    if (not (0 <= new_x < width and 0 <= new_y < height)) or (board[new_x][new_y] == 'D'):
      return (new_x - dx, new_y - dy)


def check_move(start, end):
  return not start == end


def find_start(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 'R':
        return (i, j)
def solution(board):
  dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

  start = find_start(board)
  q = deque()
  visit = set()

  for dx, dy in dxdy:
    end = find_end(board, start, (dx, dy))
    if check_move(start, end):
      q.append((start, end, 1))
      visit.add((start, end))

  while q:
    start_pop, end_pop, count = q.popleft()
    if board[end_pop[0]][end_pop[1]] == 'G':
      return count
    for dx, dy in dxdy:
      new_end = find_end(board, end_pop, (dx, dy))
      new_line = (end_pop, new_end)

      if new_end == start_pop:
        continue
      if new_line in visit:
        continue
      if not check_move(end_pop, new_end):
        continue
      q.append((end_pop, new_end, count + 1))
      visit.add(new_line)
  return -1