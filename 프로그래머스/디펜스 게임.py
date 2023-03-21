import heapq


def solution(n, k, enemy):
  answer = 0
  q = []
  for i, enm in enumerate(enemy):
    if enm > n and k == 0:
      return i
    heapq.heappush(q, (-enm, enm))
    if n < enm:
      if k > 0:
        n += heapq.heappop(q)[1] - enm
        k -= 1
    else:
      n -= enm
  return len(enemy)