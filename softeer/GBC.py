import sys


def make_table(info):
  result = [0] * 100
  index = 0
  for ran, speed in info:
    for i in range(ran):
      result[index + i] = speed
    index += ran
  return result


def solution(criteria, real):
  criteria_table = make_table(criteria)
  real_table = make_table(real)
  max_diff = -10000
  for i in range(100):
    max_diff = max(max_diff, real_table[i] - criteria_table[i])
  if max_diff < 0:
    return 0
  return max_diff


if __name__ == '__main__':
  n, m = map(int, input().split())
  criteria = []
  real = []
  for i in range(n):
    ran, speed = map(int, input().split())
    criteria.append((ran, speed))
  for i in range(m):
    ran, speed = map(int, input().split())
    real.append((ran, speed))
  print(solution(criteria, real))