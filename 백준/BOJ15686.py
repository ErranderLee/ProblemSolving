import sys
import itertools

input = sys.stdin.readline


def get_house_loc(n, arr):
  house = []
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 1:
        house.append((i, j))

  return house


def get_chicken_loc(n, arr):
  chicken = []
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 2:
        chicken.append((i, j))

  return chicken


def solution():

  n, m = map(int, input().rstrip().split())
  arr = [list(map(int, input().rstrip().split())) for i in range(n)]

  house = get_house_loc(n, arr)
  chicken = get_chicken_loc(n, arr)

  chicken_candidates = list(itertools.combinations(chicken, m))
  answer_candiates = [0] * len(chicken_candidates)

  for i, chicken_candidate in enumerate(chicken_candidates):
    for home in house:
      mini = 2500
      for chi_x, chi_y in chicken_candidate:
        mini = min(mini, abs(home[0] - chi_x) + abs(home[1] - chi_y))
      answer_candiates[i] += mini

  return min(answer_candiates)

print(solution())