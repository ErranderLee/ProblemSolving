import sys

read = sys.stdin.readline


def solution(bag_weight, jewels):
  jewels.sort(key=lambda x: (-x[1]))
  total = 0
  for w, v in jewels:
    if bag_weight >= w:
      bag_weight -= w
      total += w * v
    else:
      total += bag_weight * v
      break
  return total


bag_weight, jewel_num = map(int, read().rstrip().split(' '))
jewels = [tuple(map(int, read().rstrip().split(' '))) for _ in range(jewel_num)]

print(solution(bag_weight, jewels))