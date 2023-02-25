

def rec(a, b, c):
  if b == 1:
    return a % c
  if b % 2 == 1:
    part = rec(a, (b - 1) / 2, c) % c
    return part * part * (rec(a, 1, c) % c)
  else:
    part = rec(a, b / 2, c) % c
    return part * part


def solution(a, b, c):
  return rec(a, b, c) % c


def main():
  a, b, c = map(int, input().split())
  print(solution(a, b, c))

main()