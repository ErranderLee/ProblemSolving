import sys


def convert_key(key):
  visit = dict()
  alp = ''
  for i in range(ord('A'), ord('Z') + 1):
    an_alp = chr(i)
    if an_alp != 'J':
      visit[an_alp] = False
      alp += an_alp

  converted_key = ''
  count = 0
  for ch in key:
    if not visit[ch]:
      converted_key += ch
      visit[ch] = True
      count += 1
  # print(converted_key)

  if count < 25:
    for ch in alp:
      if not visit[ch]:
        visit[ch] = True
        converted_key += ch
        count += 1
      if count == 25:
        break
  # print(converted_key)
  result = []
  for i in range(5):
    result.append(converted_key[5 * i:5 * i + 5])
  # print(result)
  return result


def seperate_msg(msg):
  pos = 0
  result = []
  while (True):
    if pos >= len(msg):
      break
    if pos + 1 >= len(msg):
      result.append(msg[pos] + 'X')
      break
    if msg[pos] != msg[pos + 1]:
      result.append(msg[pos:pos+2])
      pos += 2
    else:
      insert_ch = 'X'
      if msg[pos] == 'X':
        insert_ch = 'Q'
      result.append(msg[pos] + insert_ch)
      pos += 1
  # print(result)
  return result


def make_cipher(seperated_msg, converted_key):
  def first_cond(chs):
    for line in converted_key:
      line = list(line)
      if chs[0] in line and chs[1] in line:
        temp = ''
        temp += line[(line.index(chs[0]) + 1) % 5]
        temp += line[(line.index(chs[1]) + 1) % 5]
        return (True, temp)
    return (False, '')


  def second_cond(chs):
    for i in range(5):
      line = ''
      for j in range(5):
        line += converted_key[j][i]
      if chs[0] in line and chs[1] in line:
        temp = ''
        temp += line[(line.index(chs[0]) + 1) % 5]
        temp += line[(line.index(chs[1]) + 1) % 5]
        return (True, temp)
    return (False, '')


  def third_cond(chs):
    first_loc, second_loc = [0, 0], [0, 0]
    for i in range(5):
      for j in range(5):
        if converted_key[i][j] == chs[0]:
          first_loc = [i, j]
        if converted_key[i][j] == chs[1]:
          second_loc = [i, j]
    return converted_key[first_loc[0]][second_loc[1]] + converted_key[second_loc[0]][first_loc[1]]


  result = ''
  for chs in seperated_msg:
    check, converted_chs = first_cond(chs)
    if check:
      result += converted_chs
      continue

    check, converted_chs = second_cond(chs)
    if check:
      result += converted_chs
      continue

    converted_chs = third_cond(chs)
    result += converted_chs

  return result


def solution(msg, key):
  converted_key = convert_key(key)
  seperated_msg = seperate_msg(msg)
  return make_cipher(seperated_msg, converted_key)


if __name__ == '__main__':
  msg = input()
  key = input()
  print(solution(msg, key))