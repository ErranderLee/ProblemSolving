import sys

dxdy = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def check_valid_pos(nx, ny, visit, jido, n):
  if not (0 <= nx < n and 0 <= ny < n):
    return False
  if (nx, ny) in visit:
    return False
  if jido[nx][ny] != 1:
    return False
  return True


def solution(n, jido):
  answer = []
  visit = set()
  for i in range(n):
    for j in range(n):
      if (i, j) in visit or jido[i][j] == 0:
        continue
      count = 1
      stack = [(i, j)]
      visit.add((i, j))
      while stack:
        x, y = stack.pop()
        for dx, dy in dxdy:
          nx = x + dx
          ny = y + dy
          if check_valid_pos(nx, ny, visit, jido, n):
            stack.append((nx, ny))
            visit.add((nx, ny))
            count += 1
      answer.append(count)

  answer.sort()
  print(len(answer))
  for num in answer:
    print(num)


read = sys.stdin.readline
n = int(read().rstrip())
jido = []
for i in range(n):
  jido.append(list(map(int, read().rstrip())))

solution(n, jido)