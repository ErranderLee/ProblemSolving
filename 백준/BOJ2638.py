import sys
from collections import deque

input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_cheese(n, m, arr):
  cheeses = set()
  for i in range(n):
    for j in range(m):
      if arr[i][j] == 1:
        cheeses.add((i, j))
  return cheeses


def melt(cheeses_to_melt, arr):
  for x, y in cheeses_to_melt:
    arr[x][y] = 0


def judge_melt(arr, n, m):
  cheeses_to_melt = set()
  for i in range(n):
    for j in range(m):
      if arr[i][j] == 1:
        exposed = 0
        for direction in directions:
          if arr[i + direction[0]][j + direction[1]] == 3:
            exposed += 1
          if exposed == 2:
            cheeses_to_melt.add((i, j))
            break

  return cheeses_to_melt


def judge_airs(n, m, arr):
  visit = [[0 for i in range(m)] for j in range(n)]
  q = deque()

  q.append((0, 0))

  while q:
    x, y = q.popleft()
    arr[x][y] = 3

    for direction in directions:
      next_x = x + direction[0]
      next_y = y + direction[1]
      if (0 <= next_x < n and 0 <= next_y < m)\
          and visit[next_x][next_y] != 1\
          and (arr[next_x][next_y] == 0 or arr[next_x][next_y] == 3):
        q.append((next_x, next_y))
        visit[next_x][next_y] = 1


def is_melt(n, m, arr):
  for i in range(n):
    for j in range(m):
      if arr[i][j] == 1:
        return False
  return True


def solution(n, m, arr):
  answer = 0

  while not is_melt(n, m, arr):
    answer += 1
    judge_airs(n, m, arr)
    cheeses_to_melt = judge_melt(arr, n, m)
    melt(cheeses_to_melt, arr)

  return answer


def main():
  n, m = map(int, input().split())
  arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

  print(solution(n, m, arr))

main()