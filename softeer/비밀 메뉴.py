import sys

m, n, k = map(int, input().split(' '))
pat = input().replace(' ', '')
user_control = input().replace(' ', '')


def solution(m, n, k, pat, user_control):
  if n < m:
    return False
  pos = 0
  while (True):
    while (True):
      if user_control[pos] == pat[0]:
        break
      pos += 1
      if pos + m > n:
        return False
    if user_control[pos:pos + m] == pat:
      return True
    pos += 1

  return False


if solution(m, n, k, pat, user_control):
  print('secret')
else:
  print('normal')