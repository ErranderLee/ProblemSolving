def get_width(s1, s2):
  long, short = max(s1, s2), min(s1, s2)
  return (long - (long - short) / 2)


def get_points(k):
  points = [k]
  while k != 1:
    rest = k % 2
    if rest == 0:
      k //= 2
    else:
      k = k * 3  + 1
    points.append(k)
  return points


def get_answer(ranges, width, length):
  answer = []
  for r in ranges:
    start = r[0]
    end = length + r[1] - 1
    if start > end or end >= length or start >= length:
      result = -1
    else:
      result = width[end]
      if r[0] > 0:
        result -= width[start]
    answer.append(result)
  return answer


def solution(k, ranges):
  points = get_points(k)
  length = len(points)
  width = [0] * length
  for i in range(1, length):
    cur = points[i]
    prev = points[i - 1]
    width[i] = width[i - 1] + get_width(cur, prev)

  return get_answer(ranges, width, length)