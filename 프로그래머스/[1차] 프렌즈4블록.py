
leftup = [(-1,0), (-1, -1), (0, -1)]
leftdown = [(0, -1), (1, 0), (1, -1)]
rightup = [(0, 1), (-1, 0), (-1, 1)]
rightdown = [(0, 1), (1, 0), (1, 1)]
def find_remove_blocks(board, remove_blocks):
  def check(i, j, direction):
    for dx, dy in direction:
      nx = i + dx
      ny = j + dy
      if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[i][j] == board[nx][ny]:
        pass
      else:
        return False
    return True
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == -1:
        continue
      if check(i, j, leftup):
        remove_blocks.add((i, j))
        for dx, dy in leftup:
          remove_blocks.add((i + dx, j + dy))

      if check(i, j, leftdown):
        remove_blocks.add((i, j))
        for dx, dy in leftdown:
          remove_blocks.add((i + dx, j + dy))

      if check(i, j, rightup):
        remove_blocks.add((i, j))
        for dx, dy in rightup:
          remove_blocks.add((i + dx, j + dy))

      if check(i, j, rightdown):
        remove_blocks.add((i, j))
        for dx, dy in rightdown:
          remove_blocks.add((i + dx, j + dy))


def remove_block(board, remove_blocks):
  for i, j in remove_blocks:
    board[i][j] = -1


def arrange(board):
  for i in range(len(board[0])):
    stack = []
    for j in range(len(board)):
      if board[j][i] == -1:
        continue
      stack.append(board[j][i])
    for j in range(len(board) - 1, -1, -1):
      if stack:
        board[j][i] = stack.pop()
      else:
        board[j][i] = -1


def solution(m, n, board):
  answer = 0
  board = [list(board[i]) for i in range(len(board))]
  while (True):
    remove_blocks = set()
    find_remove_blocks(board, remove_blocks)
    if (len(remove_blocks) == 0):
      break
    answer += len(remove_blocks)
    remove_block(board, remove_blocks)
    arrange(board)

  return answer