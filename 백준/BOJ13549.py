from collections import deque


def next_poss(pos, sec):
  return [(2 * pos, sec), (pos - 1, sec + 1), (pos + 1, sec + 1)]


def solution(n, k):
  if n > k:
    return n - k
  q = deque()
  q.append((n, 0))
  visit = set()

  while q:
    pos, sec = q.popleft()
    # print(pos, sec)
    visit.add(pos)
    if pos == k:
      return sec
    if 2 * abs(n - k) >= abs(pos - k):
      for next in next_poss(pos, sec):
        if next[0] not in visit:
          q.append(next)


if __name__ == '__main__':
  n, k = map(int, input().split())
  print(solution(n, k))