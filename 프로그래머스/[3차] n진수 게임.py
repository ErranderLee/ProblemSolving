
# 진법 변경(진법, 수)
def convert_str(n, num):
  result = []
  over_ten_map = dict()
  for i in range(0, 6):
    over_ten_map[10 + i] = chr(65 + i)
  while (num > 0):
    if num % n >= 10:
      result.append(over_ten_map[num % n])
    else:
      result.append(str(num % n))
    num //= n
  return ''.join(reversed(result))


# 진법 변경한 문자열
def get_preview_str(n, m, t):
  result = '0'
  for i in range(t * m):
    result += convert_str(n, i)
  return result


# 튜브의 순서에 해당하는 문자 리스트에 추가하기
def get_answer(p, string, t, m):
  result = ''
  turn = 0
  while (len(result) < t):
    result += string[turn * m + p - 1]
    turn += 1
  return result


def solution(n, t, m, p):
  answer = ''
  string = get_preview_str(n, m, t)
  answer = get_answer(p, string, t, m)
  return answer