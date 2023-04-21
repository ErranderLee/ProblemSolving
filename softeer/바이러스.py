import sys

divisor = 1000000007

def get_power(p, n):
  if n == 1:
    return p
  if n % 2 == 0:
    return get_power(p, n // 2) % divisor * get_power(p, n // 2) % divisor
  else:
    return get_power(p, n // 2) % divisor * get_power(p, n // 2 + 1) % divisor


def solution(k, p, n):
  # p의 n 승을 구해 k와 곱한다.
  return (get_power(p, n) * k) % divisor


if __name__ == '__main__':
  k, p, n = map(int, input().split())
  print(solution(k, p, n))